import enum as en
import typing as ty

import src.utils.gen as ugen


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

    BSLASH = en.auto()
    SEMICLN = en.auto()
    CLN = en.auto()

    SPACE = en.auto()
    TAB = en.auto()
    CARR_RET = en.auto()
    NL = en.auto()

    INT = en.auto()
    FLOAT = en.auto()
    STR = en.auto()


class Tok(ty.NamedTuple):
    typ: int
    val: str
    start: int
    end: int

    def __eq__(self, other: ty.Any) -> bool:
        if not isinstance(other, Tok):
            return False
        return (
            self.typ == other.typ
            and self.val == other.val
            and self.start == other.start
            and self.end == other.end
        )
    def __repr__(self) -> str:
        return f"{{{self.typ.name:02}: {repr(self.val)}: {self.start},{self.end}}}"


TT = TokTyps
KEYWDS = {"if", "elif", "else", "while", "for", "snoo"}
ESC_CHR_MAP = {
    "\\": "\\",
    "\'": "\'",
    "\"": "\"",
    "t": "\t",
    "r": "\r",
    "n": "\n"
}

WS = {" ", "\t", "\r", "\n"}
DIGITS = set("0123456789")
U_ALPHAS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
L_ALPHAS = set("abcdefghijklmnopqrstuvwxyz")
ALPHAS = U_ALPHAS | L_ALPHAS
VALID_WD_START_CHS = ALPHAS | {"_"}
VALID_WD_CHS = DIGITS | ALPHAS | {"_"}
VALID_NUM_CHS = DIGITS | {"."}
