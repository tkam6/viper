import enum

from src.lexer import intl as lint

LIT_TYPS = (
    lint.TT.INT,
    lint.TT.FLOAT,
    lint.TT.BOOL,
    lint.TT.STR,
    #lint.TT.IDENT,
)
UNA_OP_TYPS = (
    lint.TT.PLUS,
    lint.TT.MINUS,
    #lint.TT.AMP,
)
BIN_OP_TYPS = (
    lint.TT.PLUS,
    lint.TT.MINUS,
    lint.TT.ASTER,
    lint.TT.FSLASH,
)

ALL_GOOD = 0


class PRIM_CODES(enum.IntEnum):
    INV_EXPR = enum.auto(1)
    NO_RPAREN = enum.auto()
    INV_PRIM_TOK = enum.auto()


class UNA_CODES(enum.IntEnum):
    INV_EXPR = enum.auto(1)


class BIN_CODES(enum.IntEnum):
    INV_EXPR = enum.auto(1)
    INV_OP = enum.auto()


class LET_CODES(enum.IntEnum):
    NO_TYP = enum.auto(1)
    NO_IDENT = enum.auto()
    NO_EQ = enum.auto()
    INV_EXPR = enum.auto()
