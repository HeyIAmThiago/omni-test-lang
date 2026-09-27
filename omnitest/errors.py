"""Erros do reconhecedor, com estágio, mensagem e posição na fonte."""

from __future__ import annotations


class OmniTestError(Exception):
    def __init__(self, stage: str, message: str, line: int, column: int):
        self.stage = stage
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"{stage}: {message} (linha {line}, coluna {column})")


class OmniTestLexError(OmniTestError):
    def __init__(self, message: str, line: int, column: int):
        super().__init__("léxico", message, line, column)


class OmniTestSyntaxError(OmniTestError):
    def __init__(self, message: str, line: int, column: int):
        super().__init__("sintático", message, line, column)
