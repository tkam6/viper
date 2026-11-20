import dataclasses as dcs

from src.lexer import intl as lint


@dcs.dataclass
class BaseNode:
    pass


@dcs.dataclass
class ErrNode(BaseNode):
    code: int
    toks: list[lint.Tok]
    at: lint.Tok


@dcs.dataclass
class GrpNode(BaseNode):
    expr: list[lint.Tok]


@dcs.dataclass
class BinNode(BaseNode):
    op: lint.Tok
    lt: lint.Tok
    rt: lint.Tok


@dcs.dataclass
class UnaNode(BaseNode):
    op: lint.Tok | None
    rt: lint.Tok


@dcs.dataclass
class PrimNode(BaseNode):
    tok: lint.Tok

@dcs.dataclass
class LetNode(BaseNode):
    nm: lint.Tok
    typ: lint.Tok
    expr: GrpNode
