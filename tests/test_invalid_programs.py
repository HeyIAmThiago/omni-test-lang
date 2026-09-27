"""
tests/test_invalid_programs.py
================================

Testes automatizados (pytest) que exercitam a implementação de
referência da OmniTest contra entradas que DEVEM ser rejeitadas —
seja por erro léxico, seja por erro sintático — de acordo com a
gramática formal (ver BLOCO B, matriz de testes).

Cada caso mapeia o arquivo de entrada inválido para o tipo de exceção
esperado (OmniTestLexError ou OmniTestSyntaxError). O teste falha se a
entrada for aceita indevidamente OU se o tipo de erro relatado não
corresponder ao esperado (evitando que um erro sintático "esconda" uma
falha que deveria ser léxica, e vice-versa).
"""

from __future__ import annotations

import pathlib

import pytest

from omnitest.errors import OmniTestLexError, OmniTestSyntaxError
from omnitest.lexer import Lexer
from omnitest.parser import Parser

EXAMPLES_DIR = pathlib.Path(__file__).resolve().parent.parent / "examples"
INVALID_DIR = EXAMPLES_DIR / "invalid"


def _run(source: str):
    tokens = Lexer(source).tokenize()
    return Parser(tokens).parse_program()


# Mapa: nome do arquivo -> classe de exceção esperada.
# Ver BLOCO B (matriz de testes) para a justificativa de cada
# classificação léxica vs. sintática.
EXPECTED = {
    "indentacao_inconsistente.omt": OmniTestLexError,
    "identificador_invalido.omt": OmniTestSyntaxError,
    "token_desconhecido.omt": OmniTestLexError,
    "tipo_nao_permitido.omt": OmniTestSyntaxError,
    "comando_malformado.omt": OmniTestSyntaxError,
    "parametro_ausente.omt": OmniTestSyntaxError,
    "assercao_incompleta.omt": OmniTestSyntaxError,
    "bloco_sem_indentacao.omt": OmniTestSyntaxError,
    "dedent_inesperado.omt": OmniTestLexError,
    "eof_durante_bloco.omt": OmniTestSyntaxError,
}


@pytest.mark.parametrize("filename,expected_exc", sorted(EXPECTED.items()))
def test_entrada_invalida_e_rejeitada_com_erro_esperado(filename, expected_exc):
    path = INVALID_DIR / filename
    source = path.read_text(encoding="utf-8")
    with pytest.raises(expected_exc):
        _run(source)


def test_todos_os_arquivos_invalidos_estao_mapeados():
    """Garantia de cobertura: todo .omt em examples/invalid/ precisa ter
    uma expectativa explícita registrada acima (evita que um novo caso
    seja adicionado sem cobertura de teste)."""
    on_disk = {p.name for p in INVALID_DIR.glob("*.omt")}
    assert on_disk == set(EXPECTED.keys())


def test_mensagem_de_erro_contem_linha_e_coluna():
    """Verifica que a mensagem de erro relatada inclui localização
    (linha/coluna) e é compreensível, conforme exigido na Seção 11.4."""
    path = INVALID_DIR / "assercao_incompleta.omt"
    source = path.read_text(encoding="utf-8")
    with pytest.raises(OmniTestSyntaxError) as excinfo:
        _run(source)
    err = excinfo.value
    assert err.line == 3
    assert "linha" in str(err) and "coluna" in str(err)
