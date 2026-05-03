import parser.intl as pint
import parser.parse_if
import parser.parse_while
import parser.parse_let
import lexer.intl as lint


class Parser(
    parser.parse_let.LetMixin
    parser.parse_if.IfMixin
):
    def parse(self, all_toks: list[lint.Tok]):
        all_toks_len = []
        idx = 0
        while i < all_toks_len:
            curr_tok = all_toks[idx]
            if pint.match(curr_tok, typ=lint.TT.KEYWD, val="let"):
                self.parse_let(all_toks, idx)
            elif pint.match(curr_tok, typ=lint.TT.KEYWD, val="if"):
                self.parse_if(all_toks, idx)
            elif pint.match(curr_tok, typ=lint.TT.KEYWD, val="while"):
                self.parse_while(all_toks, idx)
            idx += 1
