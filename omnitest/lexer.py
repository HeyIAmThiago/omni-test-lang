"""Analisador léxico da OmniTest.

Emite os tokens da gramática, inclusive INDENT, DEDENT e NEWLINE.
INDENT e DEDENT não são caracteres do programa: a pilha de indentação
os produz a partir da quantidade de espaços no início de cada linha.
"""

from __future__ import annotations

from .errors import OmniTestLexError
from .tokens import KEYWORDS, Token, TokenType

_ESCAPES = {'"': '"', "\\": "\\", "n": "\n", "t": "\t"}


class Lexer:
    def __init__(self, source: str):
        self._source = source.replace("\r\n", "\n").replace("\r", "\n")
        self._lines = self._source.split("\n")
        self._tokens: list[Token] = []
        self._indent_stack: list[int] = [0]
        self._last_line = 1

    def tokenize(self) -> list[Token]:
        for line_no, raw in enumerate(self._lines, start=1):
            self._process_line(line_no, raw)

        while len(self._indent_stack) > 1:
            self._indent_stack.pop()
            self._emit(TokenType.DEDENT, "", self._last_line, 1)

        self._emit(TokenType.EOF, "", self._last_line, 1)
        return self._tokens

    def _process_line(self, line_no: int, raw: str) -> None:
        index = 0
        while index < len(raw) and raw[index] in " \t":
            if raw[index] == "\t":
                raise OmniTestLexError(
                    "tabulação não é permitida na indentação; use apenas espaços",
                    line_no,
                    index + 1,
                )
            index += 1

        if index == len(raw):
            return

        self._last_line = line_no
        self._adjust_indent(line_no, index)
        self._scan_rest(line_no, raw, index)
        self._emit(TokenType.NEWLINE, "", line_no, len(raw) + 1)

    def _adjust_indent(self, line_no: int, indent: int) -> None:
        current = self._indent_stack[-1]
        if indent == current:
            return
        if indent > current:
            self._indent_stack.append(indent)
            self._emit(TokenType.INDENT, "", line_no, 1)
            return

        while self._indent_stack[-1] > indent:
            self._indent_stack.pop()
            self._emit(TokenType.DEDENT, "", line_no, 1)

        if self._indent_stack[-1] != indent:
            raise OmniTestLexError(
                "indentação inconsistente: o recuo não coincide com nenhum nível aberto",
                line_no,
                1,
            )

    def _scan_rest(self, line_no: int, raw: str, index: int) -> None:
        while index < len(raw):
            char = raw[index]
            if char == " ":
                index += 1
                continue
            if char == "\t":
                raise OmniTestLexError(
                    "tabulação não é permitida; use apenas espaços",
                    line_no,
                    index + 1,
                )
            if char == ":":
                self._emit(TokenType.COLON, ":", line_no, index + 1)
                index += 1
                continue
            if char == ".":
                self._emit(TokenType.DOT, ".", line_no, index + 1)
                index += 1
                continue
            if char == "=":
                if index + 1 < len(raw) and raw[index + 1] == "=":
                    self._emit(TokenType.EQ, "==", line_no, index + 1)
                    index += 2
                else:
                    self._emit(TokenType.ASSIGN, "=", line_no, index + 1)
                    index += 1
                continue
            if char == '"':
                index = self._scan_string(line_no, raw, index)
                continue
            if char.isdigit():
                index = self._scan_number(line_no, raw, index)
                continue
            if char.isalpha() or char == "_":
                index = self._scan_word(line_no, raw, index)
                continue
            raise OmniTestLexError(
                f"caractere não reconhecido: {char!r}",
                line_no,
                index + 1,
            )

    def _scan_string(self, line_no: int, raw: str, index: int) -> int:
        start_column = index + 1
        index += 1
        while index < len(raw):
            char = raw[index]
            if char == '"':
                lexeme = raw[start_column - 1 : index + 1]
                self._emit(TokenType.STRING_LITERAL, lexeme, line_no, start_column)
                return index + 1
            if char == "\\":
                if index + 1 >= len(raw) or raw[index + 1] not in _ESCAPES:
                    raise OmniTestLexError(
                        "escape inválido em string; use \\\", \\\\, \\n ou \\t",
                        line_no,
                        index + 1,
                    )
                index += 2
                continue
            index += 1
        raise OmniTestLexError(
            "string não terminada na mesma linha",
            line_no,
            start_column,
        )

    def _scan_number(self, line_no: int, raw: str, index: int) -> int:
        start = index
        while index < len(raw) and raw[index].isdigit():
            index += 1
        self._emit(TokenType.INT_LITERAL, raw[start:index], line_no, start + 1)
        return index

    def _scan_word(self, line_no: int, raw: str, index: int) -> int:
        start = index
        index += 1
        while index < len(raw) and (raw[index].isalnum() or raw[index] == "_"):
            index += 1
        lexeme = raw[start:index]
        kind = KEYWORDS.get(lexeme, TokenType.IDENTIFIER)
        self._emit(kind, lexeme, line_no, start + 1)
        return index

    def _emit(self, kind: TokenType, lexeme: str, line: int, column: int) -> None:
        self._tokens.append(Token(kind, lexeme, line, column))
