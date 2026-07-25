from src.parser import intl as pint
from src.parser import ast_nodes as past
from src.lexer import intl as lint


class Parser:
    def __init__(self) -> None:
        self._toks = []
        self.len_toks = len(self.toks)
        self.idx = 0

    @property
    def toks(self):
        return self._toks

    @toks.setter
    def toks(self, val: list[lint.Tok]) -> None:
        self.len_toks = len(val)
        self._toks = val

    def adv(self) -> lint.Tok | None:
        if self.idx < self.len_toks:
            self.idx += 1

    def get(self) -> lint.Tok | None:
        if self.idx < self.len_toks:
            return self.toks[self.idx]
        return None

    def chk(self, tok_typ: lint.TokTyps, tok_val: str) -> bool:
        cur_tok = self.get()
        if cur_tok is None or cur_tok.typ != tok_typ or cur_tok.val != tok_val:
            return False
        return True

    def chk_typ(self, tok_typ: lint.TokTyps) -> bool:
        cur_tok = self.get()
        if cur_tok is None or cur_tok.typ != tok_typ:
            return False
        return True

    def chk_val(self, tok_val: str) -> bool:
        cur_tok = self.get()
        if cur_tok is None or cur_tok.val != tok_val:
            return False
        return True

    def match(self, tok_typ: lint.TokTyps, tok_val: str) -> bool:
        chk_res = self.chk(tok_typ, tok_val)
        self.idx += 1
        if chk_res:
            return chk_res

    def match_typ(self, tok_typ: lint.TokTyps) -> bool:
        chk_res = self.chk_typ(tok_typ)
        self.idx += 1
        if chk_res:
            return chk_res

    def match_val(self, tok_val: str) -> bool:
        chk_res = self.chk_val(tok_val)
        self.idx += 1
        if chk_res:
            return chk_res

    def parse_let(self) -> past.LetNode | past.ErrNode:
        # "let" keyword
        self.idx += 1
        # Type
        if not self.match_typ(lint.TT.IDENT):
            return None
        # Identifier
        if not self.match_typ(lint.TT.IDENT):
            return None
        if not self.match_typ(lint.TT.EQ):
            return None
        # if not self.get_expr():
        #     return None
        return "Boo"

    # Add function return type hint
    def parse(self, toks: list[lint.Tok]):
        self.toks = toks
        while self.get() is not None:
            if self.chk(lint.TT.KEYWD, "let"):
                print(self.parse_let())
            elif self.chk(lint.TT.KEYWD, "if"):
                print(self.parse_if())
            elif self.chk(lint.TT.KEYWD, "while"):
                print(self.parse_while())
            else:
                self.adv()
