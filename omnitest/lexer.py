"""
lexer.py
========

Analisador léxico (scanner) da linguagem OmniTest.

Responsabilidades (ver BLOCO A, Seção 6 para a especificação formal):
    1. Processar linhas físicas do código-fonte.
    2. Ignorar linhas em branco e linhas cujo único conteúdo é comentário.
    3. Medir a indentação de cada linha lógica (apenas espaços; tabs na
       indentação são erro léxico).
    4. Manter uma pilha de níveis de indentação e emitir INDENT/DEDENT.
    5. Suprimir a emissão de NEWLINE/INDENT/DEDENT enquanto o código está
       dentro de um literal JSON (chaves/colchetes abertos), de forma
       análoga à regra de continuação implícita de linha do Python dentro
       de parênteses/colchetes/chaves.
    6. Reconhecer identificadores, palavras reservadas, literais e
       operadores/delimitadores.
    7. Reportar erros léxicos com linha e coluna.
    8. Finalizar corretamente todos os blocos abertos no EOF (emitindo os
       DEDENT pendentes antes do token EOF).

Este lexer NÃO realiza nenhuma forma de análise sintática ou semântica.
Ele apenas produz uma sequência linear de tokens.
"""

from __future__ import annotations

from .errors import OmniTestLexError
from .tokens import KEYWORDS, Token, TokenType

_ID_START = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")
_ID_CONT = _ID_START | set("0123456789")
_DIGITS = set("0123456789")

_SIMPLE_ESCAPES = {
    '"': '"',
    "\\": "\\",
    "n": "\n",
    "t": "\t",
}


class Lexer:
    """Converte uma string de código-fonte OmniTest em uma lista de Token."""

    def __init__(self, source: str):
        # Normaliza terminadores de linha estilo Windows/Mac para \n.
        self._source = source.replace("\r\n", "\n").replace("\r", "\n")
        self._lines = self._source.split("\n")
        self._tokens: list[Token] = []
        self._indent_stack: list[int] = [0]
        self._bracket_depth = 0

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------
    def tokenize(self) -> list[Token]:
        for line_no, raw_line in enumerate(self._lines, start=1):
            self._process_line(line_no, raw_line)

        # Fim de arquivo: fecha blocos pendentes e detecta chaves/colchetes
        # não fechados (erro léxico, pois não há como delimitar o literal
        # JSON corretamente).
        last_line = len(self._lines) if self._lines else 1
        if self._bracket_depth > 0:
            raise OmniTestLexError(
                "fim de arquivo alcançado com '{' ou '[' sem fechamento "
                "correspondente dentro de um literal JSON",
                last_line,
                1,
            )

        while len(self._indent_stack) > 1:
            self._indent_stack.pop()
            self._tokens.append(Token(TokenType.DEDENT, "", None, last_line, 1))

        self._tokens.append(Token(TokenType.EOF, "", None, last_line, 1))
        return self._tokens

    # ------------------------------------------------------------------
    # Processamento por linha física
    # ------------------------------------------------------------------
    def _process_line(self, line_no: int, line: str) -> None:
        pos = 0

        if self._bracket_depth == 0:
            pos = self._measure_indentation(line, line_no)
            if pos is None:
                # Linha em branco ou comentário puro: nenhuma indentação
                # é avaliada, nenhum token é emitido.
                return
        # Quando bracket_depth > 0 (dentro de literal JSON), a indentação
        # é irrelevante: a linha é tratada como continuação da expressão
        # anterior (linha lógica ainda aberta).

        produced_any = self._scan_tokens(line, pos, line_no)

        if self._bracket_depth == 0 and produced_any:
            last = self._tokens[-1] if self._tokens else None
            end_col = len(line) + 1
            self._tokens.append(Token(TokenType.NEWLINE, "\n", None, line_no, end_col))

    def _measure_indentation(self, line: str, line_no: int):
        """Mede a indentação de uma linha lógica de nível zero de colchetes.

        Retorna o índice (coluna 0-based) onde o conteúdo relevante
        começa, ou None se a linha deve ser ignorada (em branco ou
        comentário puro).
        """
        i = 0
        n = len(line)
        while i < n and line[i] == " ":
            i += 1

        if i < n and line[i] == "\t":
            raise OmniTestLexError(
                "uso de caractere de tabulação (TAB) na indentação não é "
                "permitido; a OmniTest exige indentação exclusivamente "
                "com espaços",
                line_no,
                i + 1,
            )

        rest = line[i:]
        if rest == "" or rest.lstrip(" ") == "" or rest.startswith("#"):
            return None  # linha em branco ou comentário: ignorada

        indent = i
        top = self._indent_stack[-1]
        if indent > top:
            self._indent_stack.append(indent)
            self._tokens.append(Token(TokenType.INDENT, "", None, line_no, 1))
        elif indent < top:
            while self._indent_stack and indent < self._indent_stack[-1]:
                self._indent_stack.pop()
                self._tokens.append(Token(TokenType.DEDENT, "", None, line_no, i + 1))
            if self._indent_stack[-1] != indent:
                raise OmniTestLexError(
                    "indentação inconsistente: o nível de indentação "
                    f"({indent} espaços) não corresponde a nenhum nível "
                    "de indentação previamente aberto",
                    line_no,
                    i + 1,
                )
        # indent == top: mesmo nível, nenhum INDENT/DEDENT necessário.
        return i

    # ------------------------------------------------------------------
    # Reconhecimento de tokens dentro de uma linha
    # ------------------------------------------------------------------
    def _scan_tokens(self, line: str, start: int, line_no: int) -> bool:
        i = start
        n = len(line)
        produced_any = False

        while i < n:
            c = line[i]
            col = i + 1

            if c in (" ", "\t"):
                i += 1
                continue

            if c == "#":
                break  # comentário até o fim da linha física

            if c in _ID_START:
                j = i + 1
                while j < n and line[j] in _ID_CONT:
                    j += 1
                lexeme = line[i:j]
                ttype = KEYWORDS.get(lexeme, TokenType.IDENTIFIER)
                value = None
                if ttype == TokenType.BOOLEAN_LITERAL:
                    value = lexeme == "true"
                self._tokens.append(Token(ttype, lexeme, value, line_no, col))
                produced_any = True
                i = j
                continue

            if c in _DIGITS:
                j = i + 1
                while j < n and line[j] in _DIGITS:
                    j += 1
                lexeme = line[i:j]
                self._tokens.append(
                    Token(TokenType.INT_LITERAL, lexeme, int(lexeme), line_no, col)
                )
                produced_any = True
                i = j
                continue

            if c == "-" and i + 1 < n and line[i + 1] in _DIGITS:
                j = i + 2
                while j < n and line[j] in _DIGITS:
                    j += 1
                lexeme = line[i:j]
                self._tokens.append(
                    Token(TokenType.INT_LITERAL, lexeme, int(lexeme), line_no, col)
                )
                produced_any = True
                i = j
                continue

            if c == '"':
                lexeme, value, j = self._scan_string(line, i, line_no)
                self._tokens.append(
                    Token(TokenType.STRING_LITERAL, lexeme, value, line_no, col)
                )
                produced_any = True
                i = j
                continue

            if c == "=" and i + 1 < n and line[i + 1] == "=":
                self._tokens.append(Token(TokenType.EQ, "==", None, line_no, col))
                produced_any = True
                i += 2
                continue
            if c == "=":
                self._tokens.append(Token(TokenType.ASSIGN, "=", None, line_no, col))
                produced_any = True
                i += 1
                continue

            if c == "!" and i + 1 < n and line[i + 1] == "=":
                self._tokens.append(Token(TokenType.NEQ, "!=", None, line_no, col))
                produced_any = True
                i += 2
                continue

            if c == "<" and i + 1 < n and line[i + 1] == "=":
                self._tokens.append(Token(TokenType.LE, "<=", None, line_no, col))
                produced_any = True
                i += 2
                continue
            if c == "<":
                self._tokens.append(Token(TokenType.LT, "<", None, line_no, col))
                produced_any = True
                i += 1
                continue

            if c == ">" and i + 1 < n and line[i + 1] == "=":
                self._tokens.append(Token(TokenType.GE, ">=", None, line_no, col))
                produced_any = True
                i += 2
                continue
            if c == ">":
                self._tokens.append(Token(TokenType.GT, ">", None, line_no, col))
                produced_any = True
                i += 1
                continue

            if c == ".":
                self._tokens.append(Token(TokenType.DOT, ".", None, line_no, col))
                produced_any = True
                i += 1
                continue

            if c == ":":
                self._tokens.append(Token(TokenType.COLON, ":", None, line_no, col))
                produced_any = True
                i += 1
                continue

            if c == ",":
                self._tokens.append(Token(TokenType.COMMA, ",", None, line_no, col))
                produced_any = True
                i += 1
                continue

            if c == "{":
                self._bracket_depth += 1
                self._tokens.append(Token(TokenType.LBRACE, "{", None, line_no, col))
                produced_any = True
                i += 1
                continue
            if c == "}":
                self._bracket_depth -= 1
                if self._bracket_depth < 0:
                    raise OmniTestLexError(
                        "'}' encontrado sem '{' de abertura correspondente",
                        line_no,
                        col,
                    )
                self._tokens.append(Token(TokenType.RBRACE, "}", None, line_no, col))
                produced_any = True
                i += 1
                continue
            if c == "[":
                self._bracket_depth += 1
                self._tokens.append(Token(TokenType.LBRACKET, "[", None, line_no, col))
                produced_any = True
                i += 1
                continue
            if c == "]":
                self._bracket_depth -= 1
                if self._bracket_depth < 0:
                    raise OmniTestLexError(
                        "']' encontrado sem '[' de abertura correspondente",
                        line_no,
                        col,
                    )
                self._tokens.append(Token(TokenType.RBRACKET, "]", None, line_no, col))
                produced_any = True
                i += 1
                continue

            raise OmniTestLexError(
                f"caractere inesperado {c!r}; não corresponde a nenhum "
                "token válido da OmniTest",
                line_no,
                col,
            )

        # Se, ao terminar a linha, ainda houver colchetes/chaves abertos,
        # a próxima linha física é tratada como continuação lógica da
        # expressão (ver _process_line).
        return produced_any

    def _scan_string(self, line: str, start: int, line_no: int):
        """Reconhece um STRING_LITERAL a partir da aspa de abertura em
        ``start``. Suporta os escapes \\" \\\\ \\n \\t. Não permite que a
        string atravesse o fim da linha física sem ser fechada (erro
        léxico), preservando a simplicidade da tokenização.
        """
        i = start + 1
        n = len(line)
        raw_chars: list[str] = []
        while True:
            if i >= n:
                raise OmniTestLexError(
                    "string literal não foi fechada antes do fim da linha",
                    line_no,
                    start + 1,
                )
            c = line[i]
            if c == '"':
                i += 1
                break
            if c == "\\":
                if i + 1 >= n or line[i + 1] not in _SIMPLE_ESCAPES:
                    raise OmniTestLexError(
                        "sequência de escape inválida em string literal",
                        line_no,
                        i + 1,
                    )
                raw_chars.append(_SIMPLE_ESCAPES[line[i + 1]])
                i += 2
                continue
            raw_chars.append(c)
            i += 1

        lexeme = line[start:i]
        value = "".join(raw_chars)
        return lexeme, value, i
