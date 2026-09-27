"""Analisador sintático descendente recursivo da OmniTest.

Cada método consome um não-terminal da BNF documentada no README.
O parser só decide se a sequência de tokens pertence à linguagem.
"""

from __future__ import annotations

from .errors import OmniTestSyntaxError
from .tokens import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]):
        self._tokens = tokens
        self._index = 0

    def parse_program(self) -> None:
        """⟨program⟩ ::= ⟨test_decl⟩ ⟨test_decl_list⟩ EOF"""
        self._test_decl()
        self._test_decl_list()
        self._expect(TokenType.EOF)

    def _test_decl_list(self) -> None:
        """⟨test_decl_list⟩ ::= ⟨test_decl⟩ ⟨test_decl_list⟩ | ε"""
        if self._check(TokenType.TEST):
            self._test_decl()
            self._test_decl_list()

    def _test_decl(self) -> None:
        """⟨test_decl⟩ ::= "test" STRING_LITERAL ":" NEWLINE ⟨block⟩"""
        self._expect(TokenType.TEST)
        self._expect(TokenType.STRING_LITERAL)
        self._expect(TokenType.COLON)
        self._expect(TokenType.NEWLINE)
        self._block()

    def _block(self) -> None:
        """⟨block⟩ ::= INDENT ⟨stmt_list⟩ DEDENT"""
        self._expect(TokenType.INDENT)
        self._stmt_list()
        self._expect(TokenType.DEDENT)

    def _stmt_list(self) -> None:
        """⟨stmt_list⟩ ::= ⟨stmt⟩ ⟨stmt_tail⟩"""
        self._stmt()
        self._stmt_tail()

    def _stmt_tail(self) -> None:
        """⟨stmt_tail⟩ ::= ⟨stmt⟩ ⟨stmt_tail⟩ | ε"""
        if self._check(TokenType.LET) or self._check(TokenType.ASSERT):
            self._stmt()
            self._stmt_tail()

    def _stmt(self) -> None:
        """⟨stmt⟩ ::= ⟨let_stmt⟩ | ⟨assert_stmt⟩"""
        if self._check(TokenType.LET):
            self._let_stmt()
        elif self._check(TokenType.ASSERT):
            self._assert_stmt()
        else:
            token = self._peek()
            raise OmniTestSyntaxError(
                f"esperado comando let ou assert, encontrado {token.describe()}",
                token.line,
                token.column,
            )

    def _let_stmt(self) -> None:
        """⟨let_stmt⟩ ::= "let" IDENTIFIER ":" ⟨type⟩ "=" ⟨rhs⟩ NEWLINE"""
        self._expect(TokenType.LET)
        self._expect(TokenType.IDENTIFIER)
        self._expect(TokenType.COLON)
        self._type()
        self._expect(TokenType.ASSIGN)
        self._rhs()
        self._expect(TokenType.NEWLINE)

    def _type(self) -> None:
        """⟨type⟩ ::= "String" | "Int" | "Response" """
        if self._check(TokenType.TYPE_STRING, TokenType.TYPE_INT, TokenType.TYPE_RESPONSE):
            self._advance()
            return
        token = self._peek()
        raise OmniTestSyntaxError(
            f"esperado tipo String, Int ou Response, encontrado {token.describe()}",
            token.line,
            token.column,
        )

    def _rhs(self) -> None:
        """⟨rhs⟩ ::= ⟨http_request⟩ | ⟨primary⟩"""
        if self._check(TokenType.GET):
            self._http_request()
        else:
            self._primary()

    def _http_request(self) -> None:
        """⟨http_request⟩ ::= "GET" STRING_LITERAL"""
        self._expect(TokenType.GET)
        self._expect(TokenType.STRING_LITERAL)

    def _assert_stmt(self) -> None:
        """⟨assert_stmt⟩ ::= "assert" ⟨comparison⟩ NEWLINE"""
        self._expect(TokenType.ASSERT)
        self._comparison()
        self._expect(TokenType.NEWLINE)

    def _comparison(self) -> None:
        """⟨comparison⟩ ::= ⟨primary⟩ "==" ⟨primary⟩"""
        self._primary()
        self._expect(TokenType.EQ)
        self._primary()

    def _primary(self) -> None:
        """⟨primary⟩ ::= ⟨member_access⟩ | INT_LITERAL | STRING_LITERAL"""
        if self._check(TokenType.IDENTIFIER):
            self._member_access()
        elif self._check(TokenType.INT_LITERAL, TokenType.STRING_LITERAL):
            self._advance()
        else:
            token = self._peek()
            raise OmniTestSyntaxError(
                f"esperado valor, encontrado {token.describe()}",
                token.line,
                token.column,
            )

    def _member_access(self) -> None:
        """⟨member_access⟩ ::= IDENTIFIER "." IDENTIFIER"""
        self._expect(TokenType.IDENTIFIER)
        self._expect(TokenType.DOT)
        self._expect(TokenType.IDENTIFIER)

    def _check(self, *types: TokenType) -> bool:
        return self._peek().type in types

    def _expect(self, kind: TokenType) -> Token:
        token = self._peek()
        if token.type != kind:
            raise OmniTestSyntaxError(
                f"esperado {kind.value}, encontrado {token.describe()}",
                token.line,
                token.column,
            )
        return self._advance()

    def _advance(self) -> Token:
        token = self._peek()
        if token.type is not TokenType.EOF:
            self._index += 1
        return token

    def _peek(self) -> Token:
        return self._tokens[self._index]
