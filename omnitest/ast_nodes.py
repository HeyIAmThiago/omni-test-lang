"""
ast_nodes.py
============

Estruturas de dados que representam a árvore sintática (parse tree /
AST simplificada) produzida pelo parser da OmniTest quando o programa é
aceito.

Importante (transparência metodológica, ver Seção 11.4 do AGENTS.md):
esta é uma árvore sintática *concreta e simplificada*, construída
diretamente a partir das produções reconhecidas pelo parser. Ela NÃO
resulta de nenhuma etapa de análise semântica: não há resolução de tipos,
não há verificação de existência de variáveis, não há avaliação de
requisições HTTP. Cada nó apenas espelha a estrutura sintática validada.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Program:
    tests: list["TestDecl"] = field(default_factory=list)


@dataclass
class TestDecl:
    name: str
    statements: list["Stmt"]
    line: int


# Stmt é a união (conceitual) de LetStmt | AssertStmt
Stmt = object


@dataclass
class LetStmt:
    identifier: str
    type_name: str
    value: object  # HttpRequest | MemberAccess | Literal | JsonObject | JsonArray
    line: int


@dataclass
class AssertStmt:
    comparison: "Comparison"
    line: int


@dataclass
class Comparison:
    left: object
    operator: str | None  # None quando é uma comparação "nua" (apenas <primary>)
    right: object | None
    line: int


@dataclass
class HttpRequest:
    method: str  # "GET" | "POST"
    url: str
    payload: object | None  # MemberAccess, quando POST
    line: int


@dataclass
class MemberAccess:
    parts: list[str]
    line: int


@dataclass
class Literal:
    kind: str  # "int" | "string" | "bool"
    value: object
    line: int


@dataclass
class JsonObject:
    pairs: list[tuple[str, object]]
    line: int


@dataclass
class JsonArray:
    elements: list[object]
    line: int
