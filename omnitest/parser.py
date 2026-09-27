"""
parser.py
=========

Analisador sintático descendente recursivo da linguagem OmniTest.

Cada função ``_parse_<nao_terminal>`` deste módulo corresponde
diretamente a um não-terminal da gramática formal apresentada no BLOCO A
(Seção 7). O comentário acima de cada função reproduz a produção BNF que
ela implementa, permitindo checar a correspondência gramática <-> código
exigida na Seção 11.3 do AGENTS.md.

O parser consome uma lista de Token (produzida pelo Lexer) e, se a
sequência pertencer à linguagem, devolve um Program (árvore sintática).
Caso contrário, levanta OmniTestSyntaxError com linha, coluna e mensagem
explicativa.

Este parser é estritamente descendente recursivo, com no máximo 1 token
de lookahead (LL(1)) em cada ponto de decisão, EXCETO na produção
<comparison>, cuja implementação está documentada e justificada no
BLOCO A, Seção 7.5 (uso de uma forma equivalente a EBNF opcional,
resolvida por lookahead após reduzir <primary>).
"""

from __future__ import annotations

from .ast_nodes import (
    AssertStmt,
    Comparison,
    HttpRequest,
    JsonArray,
    JsonObject,
    Literal,
    LetStmt,
    MemberAccess,
    Program,
    TestDecl,
)
from .errors import OmniTestSyntaxError
from .tokens import COMPARISON_TOKENS, TYPE_TOKENS, Token, TokenType

_TYPE_NAMES = {
    TokenType.TYPE_INT: "Int",
    TokenType.TYPE_STRING: "String",
    TokenType.TYPE_BOOL: "Bool",
    TokenType.TYPE_JSON: "Json",
    TokenType.TYPE_RESPONSE: "Response",
}

_COMP_LEXEMES = {
    TokenType.EQ: "==",
    TokenType.NEQ: "!=",
    TokenType.LT: "<",
    TokenType.GT: ">",
    TokenType.LE: "<=",
    TokenType.GE: ">=",
}


class Parser:
    """Parser descendente recursivo para a gramática formal da OmniTest."""

    def __init__(self, tokens: list[Token]):
        self._tokens = tokens
        self._pos = 0

    # ------------------------------------------------------------------
    # Utilidades de consumo de tokens
    # ------------------------------------------------------------------
    def _peek(self) -> Token:
        return self._tokens[self._pos]

    def _advance(self) -> Token:
        tok = self._tokens[self._pos]
        if tok.type != TokenType.EOF:
            self._pos += 1
        return tok

    def _check(self, ttype: TokenType) -> bool:
        return self._peek().type == ttype

    def _match(self, ttype: TokenType, expected_desc: str) -> Token:
        tok = self._peek()
        if tok.type != ttype:
            raise OmniTestSyntaxError(
                f"esperado {expected_desc}, mas foi encontrado "
                f"{self._describe(tok)}",
                tok.line,
                tok.column,
            )
        return self._advance()

    @staticmethod
    def _describe(tok: Token) -> str:
        if tok.type == TokenType.EOF:
            return "fim de arquivo (EOF)"
        if tok.type == TokenType.NEWLINE:
            return "fim de linha (NEWLINE)"
        if tok.type == TokenType.INDENT:
            return "aumento de indentação (INDENT) inesperado"
        if tok.type == TokenType.DEDENT:
            return "fim de bloco (DEDENT) inesperado"
        return f"{tok.type.name} ({tok.lexeme!r})"

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------
    def parse_program(self) -> Program:
        program = self._parse_program()
        self._match(TokenType.EOF, "fim de arquivo (EOF)")
        return program

    # ------------------------------------------------------------------
    # <program> ::= <test_decl_list> EOF
    # ------------------------------------------------------------------
    def _parse_program(self) -> Program:
        tests = self._parse_test_decl_list()
        return Program(tests=tests)

    # <test_decl_list> ::= <test_decl> <test_decl_list> | ε
    def _parse_test_decl_list(self) -> list[TestDecl]:
        tests: list[TestDecl] = []
        while self._check(TokenType.TEST):
            tests.append(self._parse_test_decl())
        return tests

    # <test_decl> ::= "test" STRING_LITERAL ":" NEWLINE <block>
    def _parse_test_decl(self) -> TestDecl:
        tok = self._match(TokenType.TEST, "palavra reservada 'test'")
        name_tok = self._match(TokenType.STRING_LITERAL, "nome do cenário (string)")
        self._match(TokenType.COLON, "':' após o nome do cenário")
        self._match(TokenType.NEWLINE, "fim de linha (NEWLINE) após ':'")
        statements = self._parse_block()
        return TestDecl(name=name_tok.value, statements=statements, line=tok.line)

    # <block> ::= INDENT <stmt_list> DEDENT
    def _parse_block(self) -> list[object]:
        self._match(TokenType.INDENT, "aumento de indentação (bloco do teste)")
        statements = self._parse_stmt_list()
        self._match(TokenType.DEDENT, "fim do bloco (redução de indentação)")
        return statements

    # <stmt_list> ::= <stmt> <stmt_list> | <stmt>
    def _parse_stmt_list(self) -> list[object]:
        statements = [self._parse_stmt()]
        while self._check(TokenType.LET) or self._check(TokenType.ASSERT):
            statements.append(self._parse_stmt())
        return statements

    # <stmt> ::= <let_stmt> | <assert_stmt>
    def _parse_stmt(self):
        if self._check(TokenType.LET):
            return self._parse_let_stmt()
        if self._check(TokenType.ASSERT):
            return self._parse_assert_stmt()
        tok = self._peek()
        raise OmniTestSyntaxError(
            "esperado um comando ('let' ou 'assert') dentro do bloco de "
            f"teste, mas foi encontrado {self._describe(tok)}",
            tok.line,
            tok.column,
        )

    # <let_stmt> ::= "let" IDENTIFIER ":" <type> "=" <rhs> NEWLINE
    def _parse_let_stmt(self) -> LetStmt:
        tok = self._match(TokenType.LET, "palavra reservada 'let'")
        ident_tok = self._match(TokenType.IDENTIFIER, "identificador da variável")
        self._match(TokenType.COLON, "':' após o identificador")
        type_name = self._parse_type()
        self._match(TokenType.ASSIGN, "'=' após o tipo declarado")
        value = self._parse_rhs()
        self._match(TokenType.NEWLINE, "fim de linha (NEWLINE) após o comando 'let'")
        return LetStmt(
            identifier=ident_tok.lexeme, type_name=type_name, value=value, line=tok.line
        )

    # <assert_stmt> ::= "assert" <comparison> NEWLINE
    def _parse_assert_stmt(self) -> AssertStmt:
        tok = self._match(TokenType.ASSERT, "palavra reservada 'assert'")
        comparison = self._parse_comparison()
        self._match(TokenType.NEWLINE, "fim de linha (NEWLINE) após o comando 'assert'")
        return AssertStmt(comparison=comparison, line=tok.line)

    # <type> ::= "Int" | "String" | "Bool" | "Json" | "Response"
    def _parse_type(self) -> str:
        tok = self._peek()
        if tok.type in TYPE_TOKENS:
            self._advance()
            return _TYPE_NAMES[tok.type]
        raise OmniTestSyntaxError(
            "esperado um tipo válido ('Int', 'String', 'Bool', 'Json' ou "
            f"'Response'), mas foi encontrado {self._describe(tok)}",
            tok.line,
            tok.column,
        )

    # <rhs> ::= <http_request> | <primary>
    def _parse_rhs(self):
        if self._check(TokenType.GET) or self._check(TokenType.POST):
            return self._parse_http_request()
        return self._parse_primary()

    # <http_request> ::= "GET" STRING_LITERAL | "POST" STRING_LITERAL <primary>
    def _parse_http_request(self) -> HttpRequest:
        method_tok = self._advance()  # GET ou POST, já verificado pelo chamador
        url_tok = self._match(TokenType.STRING_LITERAL, "URL (string) da requisição HTTP")
        if method_tok.type == TokenType.GET:
            return HttpRequest(
                method="GET", url=url_tok.value, payload=None, line=method_tok.line
            )
        payload = self._parse_primary()
        return HttpRequest(
            method="POST", url=url_tok.value, payload=payload, line=method_tok.line
        )

    # <comparison> ::= <primary> <comp_op> <primary> | <primary>
    def _parse_comparison(self) -> Comparison:
        line = self._peek().line
        left = self._parse_primary()
        if self._peek().type in COMPARISON_TOKENS:
            op_tok = self._advance()
            right = self._parse_primary()
            return Comparison(
                left=left, operator=_COMP_LEXEMES[op_tok.type], right=right, line=line
            )
        return Comparison(left=left, operator=None, right=None, line=line)

    # <primary> ::= <member_access> | INT_LITERAL | STRING_LITERAL
    #             | "true" | "false" | <json_object> | <json_array>
    def _parse_primary(self):
        tok = self._peek()
        if tok.type == TokenType.IDENTIFIER:
            return self._parse_member_access()
        if tok.type == TokenType.INT_LITERAL:
            self._advance()
            return Literal(kind="int", value=tok.value, line=tok.line)
        if tok.type == TokenType.STRING_LITERAL:
            self._advance()
            return Literal(kind="string", value=tok.value, line=tok.line)
        if tok.type == TokenType.BOOLEAN_LITERAL:
            self._advance()
            return Literal(kind="bool", value=tok.value, line=tok.line)
        if tok.type == TokenType.LBRACE:
            return self._parse_json_object()
        if tok.type == TokenType.LBRACKET:
            return self._parse_json_array()
        raise OmniTestSyntaxError(
            "esperado um valor (identificador, literal inteiro, string, "
            "booleano, objeto JSON ou array JSON), mas foi encontrado "
            f"{self._describe(tok)}",
            tok.line,
            tok.column,
        )

    # <member_access> ::= IDENTIFIER <member_tail>
    # <member_tail> ::= "." IDENTIFIER <member_tail> | ε
    def _parse_member_access(self) -> MemberAccess:
        first = self._match(TokenType.IDENTIFIER, "identificador")
        parts = [first.lexeme]
        while self._check(TokenType.DOT):
            self._advance()
            part = self._match(TokenType.IDENTIFIER, "identificador após '.'")
            parts.append(part.lexeme)
        return MemberAccess(parts=parts, line=first.line)

    # <json_object> ::= "{" <json_members_opt> "}"
    def _parse_json_object(self) -> JsonObject:
        open_tok = self._match(TokenType.LBRACE, "'{' de abertura do objeto JSON")
        pairs: list[tuple[str, object]] = []
        if not self._check(TokenType.RBRACE):
            pairs = self._parse_json_members()
        self._match(TokenType.RBRACE, "'}' de fechamento do objeto JSON")
        return JsonObject(pairs=pairs, line=open_tok.line)

    # <json_members> ::= <json_pair> <json_member_tail>
    # <json_member_tail> ::= "," <json_pair> <json_member_tail> | ε
    def _parse_json_members(self) -> list[tuple[str, object]]:
        pairs = [self._parse_json_pair()]
        while self._check(TokenType.COMMA):
            self._advance()
            pairs.append(self._parse_json_pair())
        return pairs

    # <json_pair> ::= STRING_LITERAL ":" <json_value>
    def _parse_json_pair(self):
        key_tok = self._match(TokenType.STRING_LITERAL, "chave (string) do par JSON")
        self._match(TokenType.COLON, "':' entre chave e valor do par JSON")
        value = self._parse_json_value()
        return (key_tok.value, value)

    # <json_value> ::= STRING_LITERAL | INT_LITERAL | "true" | "false"
    #                | <json_object> | <json_array>
    def _parse_json_value(self):
        tok = self._peek()
        if tok.type == TokenType.STRING_LITERAL:
            self._advance()
            return Literal(kind="string", value=tok.value, line=tok.line)
        if tok.type == TokenType.INT_LITERAL:
            self._advance()
            return Literal(kind="int", value=tok.value, line=tok.line)
        if tok.type == TokenType.BOOLEAN_LITERAL:
            self._advance()
            return Literal(kind="bool", value=tok.value, line=tok.line)
        if tok.type == TokenType.LBRACE:
            return self._parse_json_object()
        if tok.type == TokenType.LBRACKET:
            return self._parse_json_array()
        raise OmniTestSyntaxError(
            "esperado um valor JSON válido (string, inteiro, booleano, "
            f"objeto ou array), mas foi encontrado {self._describe(tok)}",
            tok.line,
            tok.column,
        )

    # <json_array> ::= "[" <json_elements_opt> "]"
    def _parse_json_array(self) -> JsonArray:
        open_tok = self._match(TokenType.LBRACKET, "'[' de abertura do array JSON")
        elements: list[object] = []
        if not self._check(TokenType.RBRACKET):
            elements = self._parse_json_elements()
        self._match(TokenType.RBRACKET, "']' de fechamento do array JSON")
        return JsonArray(elements=elements, line=open_tok.line)

    # <json_elements> ::= <json_value> <json_element_tail>
    # <json_element_tail> ::= "," <json_value> <json_element_tail> | ε
    def _parse_json_elements(self) -> list[object]:
        elements = [self._parse_json_value()]
        while self._check(TokenType.COMMA):
            self._advance()
            elements.append(self._parse_json_value())
        return elements
