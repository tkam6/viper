import enum
import typing as ty

from src.utils import gen as ugen


class TokTyps(enum.IntEnum):
    INV = 0
    KEYWD = enum.auto()
    IDENT = enum.auto()

    EQ = enum.auto()
    PLUS = enum.auto()
    MINUS = enum.auto()
    ASTER = enum.auto()
    FSLASH = enum.auto()
    EQEQ = enum.auto()
    NOTEQ = enum.auto()
    LT = enum.auto()
    LTEQ = enum.auto()
    GT = enum.auto()
    GTEQ = enum.auto()
    AMP = enum.auto()
    PIPE = enum.auto()
    EXCLM = enum.auto()
    DOU_AMP = enum.auto()
    DOU_PIPE = enum.auto()
    DOU_LT = enum.auto()
    DOU_GT = enum.auto()

    LPAREN = enum.auto()
    RPAREN = enum.auto()
    LBRACE = enum.auto()
    RBRACE = enum.auto()
    LBRACK = enum.auto()
    RBRACK = enum.auto()

    BSLASH = enum.auto()
    SEMICLN = enum.auto()
    CLN = enum.auto()

    SPACE = enum.auto()
    TAB = enum.auto()
    CARR_RET = enum.auto()
    NL = enum.auto()

    INT = enum.auto()
    FLOAT = enum.auto()
    BOOL = enum.auto()
    STR = enum.auto()


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
        return f"{{{self.typ.name:02}: {self.val!r}: {self.start},{self.end}}}"


TT = TokTyps
KEYWDS = {"if", "elif", "else", "while", "for", "snoo", "let"}
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
