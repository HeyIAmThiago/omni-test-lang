"""Casos ligados aos dois exemplos da entrega."""

from pathlib import Path

import pytest

from omnitest import OmniTestError, recognize

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"


def test_get_one_aceito():
    recognize((EXAMPLES / "get_one.omt").read_text(encoding="utf-8"))


def test_get_all_aceito():
    recognize((EXAMPLES / "get_all.omt").read_text(encoding="utf-8"))


def test_indentacao_inconsistente_rejeitada():
    source = (
        'test "indent":\n'
        '    let response: Response = GET "https://jsonplaceholder.typicode.com/posts/1"\n'
        "  assert response.status == 200\n"
    )
    with pytest.raises(OmniTestError) as exc:
        recognize(source)
    assert exc.value.stage == "léxico"


def test_comando_malformado_rejeitado():
    source = (
        'test "ruim":\n'
        '    let response Response = GET "https://jsonplaceholder.typicode.com/posts/1"\n'
    )
    with pytest.raises(OmniTestError) as exc:
        recognize(source)
    assert exc.value.stage == "sintático"


def test_palavra_reservada_no_lugar_de_variavel_rejeitada():
    source = 'test "nome":\n    let test: Int = 1\n    assert test == 1\n'
    with pytest.raises(OmniTestError) as exc:
        recognize(source)
    assert exc.value.stage == "sintático"
