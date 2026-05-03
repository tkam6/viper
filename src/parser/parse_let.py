import parser.ast_nodes as past
import parser.err as perr
import parser.intl as pint
import lexer.intl as lint


class LetMixin:
    def parse_let(
        self,
        all_toks: list[lint.Tok],
        all_toks_len: int,
        idx: int
    ) -> past.LetNode | past.ErrNode:
        start = idx
        # For the keyword 'let'
        idx += 1
        if not pint.match(all_toks[idx], typ=lint.TT.IDENT):
            return past.ErrNode(err=perr.LetNode.EXPD_IDENT, toks=all_toks[start : idx + 1])
