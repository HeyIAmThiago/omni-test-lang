"""
tests/test_valid_programs.py
=============================

Testes automatizados (pytest) que exercitam a implementação de
referência da OmniTest contra entradas que DEVEM ser aceitas pela
gramática formal (ver BLOCO B, matriz de testes).

Cada teste aqui foi de fato executado como parte da entrega (não são
resultados hipotéticos): rodar `pytest -v` neste diretório reproduz os
mesmos resultados relatados no BLOCO B.
"""

from __future__ import annotations

import pathlib

import pytest

from omnitest.ast_nodes import JsonArray
from omnitest.lexer import Lexer
from omnitest.parser import Parser
from omnitest.tokens import TokenType

EXAMPLES_DIR = pathlib.Path(__file__).resolve().parent.parent / "examples"
VALID_DIR = EXAMPLES_DIR / "valid"


def _accept(source: str):
    tokens = Lexer(source).tokenize()
    program = Parser(tokens).parse_program()
    return tokens, program


# ---------------------------------------------------------------------
# T-V01: Exemplo 1 obrigatório da Seção 10 — GET + Response + assert
# ---------------------------------------------------------------------
def test_exemplo1_get_test_e_aceito():
    source = (EXAMPLES_DIR / "get_test.omt").read_text(encoding="utf-8")
    _, program = _accept(source)
    assert len(program.tests) == 1
    test = program.tests[0]
    assert test.name == "health check retorna 200"
    assert len(test.statements) == 2  # let + assert


# ---------------------------------------------------------------------
# T-V02: Exemplo 2 obrigatório da Seção 10 — POST + payload JSON
# ---------------------------------------------------------------------
def test_exemplo2_post_test_e_aceito():
    source = (EXAMPLES_DIR / "post_test.omt").read_text(encoding="utf-8")
    _, program = _accept(source)
    assert len(program.tests) == 1
    test = program.tests[0]
    # let payload + let response + assert status + assert body.name
    assert len(test.statements) == 4


# ---------------------------------------------------------------------
# T-V03: programa mínimo válido (um único assert)
# ---------------------------------------------------------------------
def test_minimo_valido():
    source = (VALID_DIR / "minimo_valido.omt").read_text(encoding="utf-8")
    _, program = _accept(source)
    assert len(program.tests) == 1
    assert len(program.tests[0].statements) == 1


# ---------------------------------------------------------------------
# T-V04: declaração de variável tipada válida
# ---------------------------------------------------------------------
def test_declaracao_variavel_valida():
    source = (VALID_DIR / "declaracao_variavel.omt").read_text(encoding="utf-8")
    tokens, program = _accept(source)
    let_stmt = program.tests[0].statements[0]
    assert let_stmt.identifier == "statusEsperado"
    assert let_stmt.type_name == "Int"


# ---------------------------------------------------------------------
# T-V05 / T-V07: múltiplos testes sequenciais == múltiplos níveis de
# indentação (abre e fecha a pilha de indentação mais de uma vez) e
# programa com múltiplos comandos.
# ---------------------------------------------------------------------
def test_multiplos_testes_e_multiplos_niveis_indentacao():
    source = (VALID_DIR / "multiplos_testes.omt").read_text(encoding="utf-8")
    tokens, program = _accept(source)
    assert len(program.tests) == 2
    assert len(program.tests[0].statements) == 2
    assert len(program.tests[1].statements) == 4

    indent_count = sum(1 for t in tokens if t.type == TokenType.INDENT)
    dedent_count = sum(1 for t in tokens if t.type == TokenType.DEDENT)
    assert indent_count == 2
    assert dedent_count == 2


# ---------------------------------------------------------------------
# T-V06: JSON literal em múltiplas linhas físicas (continuação implícita
# de linha dentro de chaves/colchetes — NEWLINE suprimido).
# ---------------------------------------------------------------------
def test_json_multilinha_suprime_newline_interno():
    source = (VALID_DIR / "json_multilinha.omt").read_text(encoding="utf-8")
    tokens, program = _accept(source)
    let_stmt = program.tests[0].statements[0]
    assert let_stmt.type_name == "Json"
    json_obj = let_stmt.value
    assert [k for k, _ in json_obj.pairs] == ["name", "roles", "active"]
    # Exatamente 1 NEWLINE por linha lógica: o objeto JSON de 5 linhas
    # físicas produz UMA única linha lógica de comando (não 5).
    newline_count = sum(1 for t in tokens if t.type == TokenType.NEWLINE)
    # 1 (header do test) + 1 (fechamento do let com json multilinha)
    # + 1 (let response) + 1 (assert) = 4
    assert newline_count == 4


# ---------------------------------------------------------------------
# T-V07b: array JSON como valor de nível superior de uma variável Json
# (correção aplicada durante a revisão crítica obrigatória — ver BLOCO D)
# ---------------------------------------------------------------------
def test_json_array_como_valor_de_nivel_superior():
    source = (VALID_DIR / "json_array_nivel_superior.omt").read_text(encoding="utf-8")
    _, program = _accept(source)
    let_stmt = program.tests[0].statements[0]
    assert isinstance(let_stmt.value, JsonArray)
    assert [el.value for el in let_stmt.value.elements] == ["QA", "SDET", "Automation"]


# ---------------------------------------------------------------------
# T-V08: programa vazio (política: sintaticamente válido, zero testes)
# ---------------------------------------------------------------------
def test_programa_vazio_e_aceito_pela_politica_definida():
    source = (VALID_DIR / "programa_vazio.omt").read_text(encoding="utf-8")
    tokens, program = _accept(source)
    assert program.tests == []
    assert tokens[-1].type == TokenType.EOF


# ---------------------------------------------------------------------
# Varredura genérica: todo arquivo em examples/valid/*.omt deve ser
# aceito sem levantar exceção.
# ---------------------------------------------------------------------
@pytest.mark.parametrize(
    "path", sorted(VALID_DIR.glob("*.omt")), ids=lambda p: p.name
)
def test_todos_os_exemplos_validos_sao_aceitos(path: pathlib.Path):
    source = path.read_text(encoding="utf-8")
    _accept(source)  # não deve levantar exceção
