"""
Ponto de entrada de linha de comando da implementação de referência.

Uso:
    python -m omnitest <arquivo.omt>

Resultado:
    * Se o arquivo for aceito, imprime "ACEITO" e um resumo da árvore
      sintática (quantidade de testes e comandos reconhecidos).
    * Se houver erro léxico ou sintático, imprime "REJEITADO" seguido da
      mensagem de erro (estágio, descrição, linha e coluna) e finaliza
      com código de saída 1.

Este script NÃO executa nenhuma requisição HTTP e NÃO realiza nenhuma
verificação semântica: ele apenas relata se a entrada pertence ou não à
linguagem formalmente definida para a OmniTest.
"""

from __future__ import annotations

import sys

from .errors import OmniTestError
from .lexer import Lexer
from .parser import Parser


def run_file(path: str) -> int:
    with open(path, "r", encoding="utf-8") as fh:
        source = fh.read()

    try:
        tokens = Lexer(source).tokenize()
        program = Parser(tokens).parse_program()
    except OmniTestError as exc:
        print("REJEITADO")
        print(str(exc))
        return 1

    n_tests = len(program.tests)
    n_stmts = sum(len(t.statements) for t in program.tests)
    print("ACEITO")
    print(f"Testes reconhecidos: {n_tests}")
    print(f"Comandos reconhecidos: {n_stmts}")
    for t in program.tests:
        print(f'  - test "{t.name}" (linha {t.line}): {len(t.statements)} comando(s)')
    return 0


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Uso: python -m omnitest <arquivo.omt>")
        return 2
    return run_file(argv[1])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
