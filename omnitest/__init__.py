"""Reconhecedor da OmniTest: aceita ou rejeita um código-fonte."""

from .errors import OmniTestError
from .lexer import Lexer
from .parser import Parser


def recognize(source: str) -> None:
    """Levanta OmniTestError se o código não pertence à linguagem."""
    Parser(Lexer(source).tokenize()).parse_program()


__all__ = ["OmniTestError", "recognize"]
