"""Garante que o pacote `omnitest`, localizado na raiz deste repositório,
seja importável pelos módulos de teste em `tests/`, independentemente do
diretório a partir do qual o pytest é invocado.
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
