"""
tokens.py
=========

Define o conjunto fechado de categorias de token (TokenType) e a estrutura
de dado Token utilizada pelo lexer e pelo parser da linguagem OmniTest.

Este módulo é a "fonte única da verdade" sobre quais terminais existem na
gramática formal (ver BLOCO A, Seção 7). Qualquer terminal citado na
gramática BNF deve possuir um TokenType correspondente aqui, e vice-versa
— nenhum token é definido "sobrando" sem uso na gramática.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    # ---- Estruturais (gerados pelo controle de indentação/linha) --------
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()

    # ---- Identificador e literais ---------------------------------------
    IDENTIFIER = auto()
    INT_LITERAL = auto()
    STRING_LITERAL = auto()
    BOOLEAN_LITERAL = auto()

    # ---- Palavras reservadas de estrutura de teste ----------------------
    TEST = auto()
    LET = auto()
    ASSERT = auto()

    # ---- Palavras reservadas de método HTTP -----------------------------
    GET = auto()
    POST = auto()

    # ---- Palavras reservadas de tipo ------------------------------------
    TYPE_INT = auto()
    TYPE_STRING = auto()
    TYPE_BOOL = auto()
    TYPE_JSON = auto()
    TYPE_RESPONSE = auto()

    # ---- Operadores --------------------------------------------------
    ASSIGN = auto()     # =
    EQ = auto()         # ==
    NEQ = auto()        # !=
    LT = auto()         # <
    GT = auto()         # >
    LE = auto()         # <=
    GE = auto()         # >=
    DOT = auto()        # .

    # ---- Delimitadores -----------------------------------------------
    COLON = auto()       # :
    COMMA = auto()       # ,
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    LBRACKET = auto()     # [
    RBRACKET = auto()     # ]


# Palavras reservadas da OmniTest. Mapeia o lexema exato (case-sensitive)
# para o TokenType correspondente. Qualquer identificador cujo lexema
# coincida com uma destas chaves é classificado como palavra reservada,
# nunca como IDENTIFIER (ver BLOCO A, Seção 6.2).
KEYWORDS: dict[str, TokenType] = {
    "test": TokenType.TEST,
    "let": TokenType.LET,
    "assert": TokenType.ASSERT,
    "GET": TokenType.GET,
    "POST": TokenType.POST,
    "Int": TokenType.TYPE_INT,
    "String": TokenType.TYPE_STRING,
    "Bool": TokenType.TYPE_BOOL,
    "Json": TokenType.TYPE_JSON,
    "Response": TokenType.TYPE_RESPONSE,
    "true": TokenType.BOOLEAN_LITERAL,
    "false": TokenType.BOOLEAN_LITERAL,
}

# Conjunto de tipos primitivos válidos na linguagem (usado pelo parser
# para validar a produção <type>).
TYPE_TOKENS = {
    TokenType.TYPE_INT,
    TokenType.TYPE_STRING,
    TokenType.TYPE_BOOL,
    TokenType.TYPE_JSON,
    TokenType.TYPE_RESPONSE,
}

COMPARISON_TOKENS = {
    TokenType.EQ,
    TokenType.NEQ,
    TokenType.LT,
    TokenType.GT,
    TokenType.LE,
    TokenType.GE,
}


@dataclass(frozen=True)
class Token:
    """Representa um token emitido pelo lexer.

    Atributos:
        type: categoria do token (TokenType).
        lexeme: texto literal reconhecido na fonte (string vazia para
            tokens estruturais sintéticos como INDENT/DEDENT/EOF).
        value: valor semântico já convertido quando aplicável (ex.: int
            para INT_LITERAL, bool para BOOLEAN_LITERAL, str decodificada
            para STRING_LITERAL). None nos demais casos.
        line: linha (1-indexada) onde o token começa no código-fonte.
        column: coluna (1-indexada) onde o token começa no código-fonte.
    """

    type: TokenType
    lexeme: str
    value: object
    line: int
    column: int

    def __repr__(self) -> str:  # pragma: no cover - apenas depuração
        return f"Token({self.type.name}, {self.lexeme!r}, L{self.line}:C{self.column})"
