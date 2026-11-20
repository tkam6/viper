import enum

from src.lexer import intl as lint
from src.parser import ast_nodes as past
from src.parser import intl as pint


class Parser:
    def __init__(self) -> None:
        self._toks = []
        self.len_toks = len(self.toks)
        self.idx = 0

        self.tok_rng = lambda start: self.toks[start : self.idx]

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
        return (
            (cur_tok := self.get()) is not None
            and cur_tok.typ == tok_typ
            and cur_tok.val == tok_val
        )

    def chk_typ(self, tok_typ: lint.TokTyps) -> bool:
        return (cur_tok := self.get()) is not None and cur_tok.typ == tok_typ

    def chk_val(self, tok_val: str) -> bool:
        return (cur_tok := self.get()) is not None and cur_tok.val == tok_val

    def match(self, tok_typ: lint.TokTyps, tok_val: str) -> lint.Tok | None:
        tok = self.get()
        if self.chk(tok_typ, tok_val):
            self.idx += 1
            return tok
        return None

    def match_typ(self, tok_typ: lint.TokTyps) -> lint.Tok | None:
        tok = self.get()
        if self.chk_typ(tok_typ):
            self.idx += 1
            return tok
        return None

    def match_val(self, tok_val: str) -> lint.Tok | None:
        tok = self.get()
        if self.chk_val(tok_val):
            self.idx += 1
            return tok
        return None

    def match_typ_multi(self, tok_typs: list[lint.TokTyps]) -> lint.Tok | None:
        for typ in tok_typs:
            tmp = self.match_typ(typ)
            if tmp is not None:
                return tmp
        return None

    def get_expr(self):
        lt = self.get_expr()
        raise NotImplementedError

    def get_bin_op(self):
        start = self.idx
        # left operand
        lt = self.get_unary_op()
        if isinstance(lt, past.ErrNode):
            return past.ErrNode(pint.BIN_CODES.INV_EXPR, self.tok_rng(start), self.get())
        # operator
        if (op := self.match_typ_multi(pint.BIN_OP_TYPS)) is None:
            return lt
        # right operand
        rt = self.get_bin_op()
        if isinstance(rt, past.ErrNode):
            return past.ErrNode(pint.BIN_CODES.INV_EXPR, self.tok_rng(start), self.get())
        return past.BinNode(op, lt, rt)

    def get_unary_op(self):
        start = self.idx
        # operator
        if (op := self.match_typ_multi(pint.UNA_OP_TYPS)) is None:
            return self.get_prim()
        # operand
        rt = self.get_unary_op()
        if isinstance(rt, past.ErrNode):
            return past.ErrNode(pint.UNA_CODES.INV_EXPR, self.tok_rng(start), rt.at)
        return past.UnaNode(op, rt)

    def get_prim(self):
        start = self.idx
        # literal or identifier
        if (tok := self.match_typ_multi(pint.LIT_TYPS + (lint.TT.IDENT,))):
            return past.PrimNode(tok)
        # parenthesised expression
        elif tok := self.match_typ(lint.LPAREN):
            expr = self.get_bin_op()
            if isinstance(expr, past.ErrNode):
                return past.ErrNode(pint.PRIM_CODES.INV_EXPR, self.tok_rng(start), expr.at)
            if self.match_typ(lint.RPAREN) is None:
                return past.ErrNode(pint.PRIM_CODES.NO_RPAREN, self.tok_rng(start), expr.get())
            return expr
        return past.ErrNode(pint.PRIM_CODES.INV_PRIM_TOK, self.tok_rng(start), self.get())

    def parse_let(self) -> past.LetNode | past.ErrNode:
        "let <type> <ident> = <expr>"
        code = pint.ALL_GOOD
        start = self.idx
        if self.match(lint.TT.KEYWD, "let") is None:
            code = pint.LET_CODES.NO_KEYWD
        if (typ := self.match_typ(lint.TT.IDENT)) is None:
            code = pint.LET_CODES.NO_TYP
        if (nm := self.match_typ(lint.TT.IDENT)) is None:
            code = pint.LET_CODES.NO_IDENT
        if self.match_typ(lint.TT.EQ) is None:
            code = pint.LET_CODES.NO_EQ
        expr = self.get_bin_op()
        if isinstance(expr, past.ErrNode):
            code = pint.LET_CODES.INV_EXPR

        if code != pint.ALL_GOOD:
            return past.ErrNode(self.tok_rng(start), code, self.get())
        return past.LetNode(nm, typ, expr)

    # Add function return type hint
    def parse(self, toks: list[lint.Tok]):
        self.toks = toks
        while self.get() is not None:
            #print(self.chk(lint.TT.KEYWD, "let"))
            if self.chk(lint.TT.KEYWD, "let"):
                print(self.parse_let())
            #elif self.chk(lint.TT.KEYWD, "if"):
            #    print(self.parse_if())
            #elif self.chk(lint.TT.KEYWD, "while"):
            #    print(self.parse_while())
            else:
                self.adv()
