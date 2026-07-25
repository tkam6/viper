import dataclasses as dcs
from src.lexer import intl as lint


@dcs.dataclass
class ErrNode:
    err: int
    toks: list[lint.Tok]

@dcs.dataclass
class LetNode:
    nm: str
    val: str
    toks: list[lint.Tok]


class GrpNode:
    pass
