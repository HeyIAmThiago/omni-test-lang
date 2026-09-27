"""
errors.py
=========

Define as exceções usadas para reportar erros léxicos e sintáticos da
OmniTest, sempre com localização (linha/coluna) e mensagem compreensível,
conforme exigido na Seção 11.4 do prompt master (AGENTS.md).

Este projeto NÃO implementa análise semântica; portanto não existe uma
classe de erro semântico. Essa ausência é deliberada e está documentada
no BLOCO A (Seção 9) e no BLOCO D (auditoria).
"""

from __future__ import annotations


class OmniTestError(Exception):
    """Classe base para todos os erros reportáveis do compilador OmniTest."""

    def __init__(self, message: str, line: int, column: int):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.__str__())

    def __str__(self) -> str:
        return f"{self.stage()}: {self.message} (linha {self.line}, coluna {self.column})"

    def stage(self) -> str:  # pragma: no cover - sobrescrito nas subclasses
        return "Erro"


class OmniTestLexError(OmniTestError):
    """Erro detectado durante a análise léxica.

    Exemplos de causas: caractere não reconhecido, string não fechada,
    indentação inconsistente (mistura de espaços/tabs ou nível de
    indentação que não corresponde a nenhum nível da pilha), literal
    numérico malformado.
    """

    def stage(self) -> str:
        return "Erro léxico"


class OmniTestSyntaxError(OmniTestError):
    """Erro detectado durante a análise sintática.

    Levantado quando a sequência de tokens não corresponde a nenhuma
    derivação válida da gramática formal da OmniTest (ver BLOCO A,
    Seção 7).
    """

    def stage(self) -> str:
        return "Erro sintático"
