"""Reconhece um arquivo OmniTest.

Uso:
    python -m omnitest <arquivo.omt>
"""

from __future__ import annotations

import sys

from .errors import OmniTestError
from . import recognize


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("uso: python -m omnitest <arquivo.omt>", file=sys.stderr)
        return 2

    try:
        with open(args[0], encoding="utf-8") as source_file:
            source = source_file.read()
        recognize(source)
    except OSError as exc:
        print(f"não foi possível ler o arquivo: {exc}", file=sys.stderr)
        return 2
    except OmniTestError as exc:
        print("REJEITADO")
        print(exc)
        return 1

    print("ACEITO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
