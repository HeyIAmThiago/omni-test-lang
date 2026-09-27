"""
OmniTest — implementação de referência (Projeto de Compiladores, Parte 1).

Este pacote contém uma implementação executável, em Python puro (biblioteca
padrão apenas), de um analisador léxico (lexer) e de um analisador sintático
descendente recursivo (parser) para a linguagem OmniTest.

Escopo efetivamente implementado:
    * Análise léxica completa (tokens, indentação, erros léxicos).
    * Análise sintática completa (reconhecimento da gramática formal,
      construção de uma árvore sintática simplificada / AST).

Escopo explicitamente NÃO implementado nesta entrega (P1):
    * Análise semântica (verificação de tipos, escopos, existência de
      variáveis).
    * Execução real de requisições HTTP.
    * Geração de código objeto ou qualquer etapa de back-end.

Consulte o BLOCO A / BLOCO B da entrega para a justificativa dessas
decisões de escopo.
"""

from .tokens import Token, TokenType
from .errors import OmniTestLexError, OmniTestSyntaxError
from .lexer import Lexer
from .parser import Parser

__all__ = [
    "Token",
    "TokenType",
    "OmniTestLexError",
    "OmniTestSyntaxError",
    "Lexer",
    "Parser",
]
