"""Tokens usados pela gramática da OmniTest."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    TEST = "test"
    LET = "let"
    ASSERT = "assert"
    GET = "GET"
    TYPE_STRING = "String"
    TYPE_INT = "Int"
    TYPE_RESPONSE = "Response"
    IDENTIFIER = "IDENTIFIER"
    INT_LITERAL = "INT_LITERAL"
    STRING_LITERAL = "STRING_LITERAL"
    ASSIGN = "="
    EQ = "=="
    DOT = "."
    COLON = ":"
    NEWLINE = "NEWLINE"
    INDENT = "INDENT"
    DEDENT = "DEDENT"
    EOF = "EOF"


KEYWORDS = {
    "test": TokenType.TEST,
    "let": TokenType.LET,
    "assert": TokenType.ASSERT,
    "GET": TokenType.GET,
    "String": TokenType.TYPE_STRING,
    "Int": TokenType.TYPE_INT,
    "Response": TokenType.TYPE_RESPONSE,
}


@dataclass(frozen=True)
class Token:
    type: TokenType
    lexeme: str
    line: int
    column: int

    def describe(self) -> str:
        if self.type in {
            TokenType.NEWLINE,
            TokenType.INDENT,
            TokenType.DEDENT,
            TokenType.EOF,
        }:
            return self.type.value
        if self.lexeme:
            return f"{self.type.value} ({self.lexeme!r})"
        return self.type.value
