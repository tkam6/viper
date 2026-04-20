import enum as en
import typing as ty

import utils.gen as ugen

iota_cntr = 0


def iota(reset: bool = False) -> int:
    global iota_cntr
    if reset:
        iota_cntr = 0
    res = iota_cntr
    iota_cntr += 1
    return res


class TokTyps(en.IntEnum):
    INV = 0
    KEYWD = en.auto()
    IDENT = en.auto()

    EQ = en.auto()
    PLUS = en.auto()
    MINUS = en.auto()
    ASTER = en.auto()
    FSLASH = en.auto()
    EQEQ = en.auto()
    NOTEQ = en.auto()
    LT = en.auto()
    LTEQ = en.auto()
    GT = en.auto()
    GTEQ = en.auto()
    AMP = en.auto()
    PIPE = en.auto()
    EXCLM = en.auto()
    DOU_AMP = en.auto()
    DOU_PIPE = en.auto()
    DOU_LT = en.auto()
    DOU_GT = en.auto()

    INT = en.auto()
    FLOAT = en.auto()
    STR = en.auto()


class Tok(ty.NamedTuple):
    typ: int
    val: str
    start: int
    end: int

    def __repr__(self) -> str:
        return f"{{{self.typ:02}: {self.val}}}"


class NoCloseQuote(ugen.Err):
    pass


TT = TokTyps
WS = {" ", "\t", "\r", "\n"}
DIGITS = set("0123456789")
U_ALPHAS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
L_ALPHAS = set("abcdefghijklmnopqrstuvwxyz")
ALPHAS = U_ALPHAS | L_ALPHAS
VALID_WD_START_CHS = ALPHAS | {"_"}
VALID_WD_CHS = DIGITS | ALPHAS | {"_"}
VALID_NUM_CHS = DIGITS | {"."}
KEYWDS = {"if", "elif", "else", "while", "for"}
