import lexer.intl as lint


class Lexer:
    def _skip_ws(self, src: str, src_len: int, idx: int) -> int:
        while idx < src_len:
            if src[idx].isspace():
                idx += 1
                continue
            break
        return idx

    def _get_num(self, src: str, src_len: int, idx: int) -> lint.Tok:
        start = idx
        dot_cnt = 0
        while idx < src_len:
            ch = src[idx]
            if ch not in lint.VALID_NUM_CHS:
                break
            if ch == ".":
                dot_cnt += 1
            if dot_cnt > 1:
                break
            idx += 1
        val = src[start : idx]
        # Value ends with '.'; eject the dot and report only integral part
        if val.endswith("."):
            return lint.Tok(lint.TT.INT, val[: -1], start, idx - 1)
        if dot_cnt:
            return lint.Tok(lint.TT.FLOAT, src[start : idx], start, idx)
        return lint.Tok(lint.TT.INT, src[start : idx], start, idx)

    def _get_str(self, src: str, src_len: int, idx: int) -> lint.Tok:
        start = idx
        # For starting quote
        idx += 1
        while idx < src_len:
            ch = src[idx]
            if ch == "\"":
                break
            if ch in lint.WS:
                return lint.Tok(lint.TT.INV, src[start : idx], start, idx)
            idx += 1
        # idx + 1 for end value to accommodate ending quote
        val = src[start : idx + 1]
        return lint.Tok(lint.TT.STR, val, start, idx + 1)

    def _get_wd(self, src: str, src_len: int, idx: int) -> lint.Tok:
        start = idx
        while idx < src_len:
            ch = src[idx]
            if ch not in lint.VALID_WD_CHS:
                break
            idx += 1
        val = src[start : idx]
        if val in lint.KEYWDS:
            return lint.Tok(lint.TT.KEYWD, val, start, idx)
        return lint.Tok(lint.TT.IDENT, val, start, idx)

    def lex(self, src: str) -> list[lint.Tok]:
        src_len = len(src)
        all_toks = []
        chk_nxt_ch = lambda ch: idx < src_len - 1 and src[idx + 1] == ch
        # Ignore leading whitespace
        idx = self._skip_ws(src, src_len, 0)

        while idx < src_len:
            ch = src[idx]

            if ch == "+":
                tok = lint.Tok(lint.TT.PLUS, "+", idx, idx + 1)
            elif ch == "-":
                tok = lint.Tok(lint.TT.MINUS, "-", idx, idx + 1)
            elif ch == "*":
                tok = lint.Tok(lint.TT.ASTER, "*", idx, idx + 1)
            elif ch == "/":
                tok = lint.Tok(lint.TT.FSLASH, "/", idx, idx + 1)
            elif ch == "&":
                tok = lint.Tok(lint.TT.AMP, "&", idx, idx + 1)
                if chk_nxt_ch("&"):
                    tok = lint.Tok(lint.TT.DOU_AMP, "&&", idx, idx + 2)
            elif ch == "|":
                tok = lint.Tok(lint.TT.PIPE, "|", idx, idx + 1)
                if chk_nxt_ch("|"):
                    tok = lint.Tok(lint.TT.DOU_PIPE, "||", idx, idx + 2)
            elif ch == "<":
                tok = lint.Tok(lint.TT.LT, "<", idx, idx + 1)
                if chk_nxt_ch("="):
                    tok = lint.Tok(lint.TT.LTEQ, "<=", idx, idx + 2)
                elif chk_nxt_ch("<"):
                    tok = lint.Tok(lint.TT.DOU_LT, "<<", idx, idx + 2)
            elif ch == ">":
                tok = lint.Tok(lint.TT.GT, ">", idx, idx + 1)
                if chk_nxt_ch("="):
                    tok = lint.Tok(lint.TT.GTEQ, ">=", idx, idx + 2)
                elif chk_nxt_ch(">"):
                    tok = lint.Tok(lint.TT.DOU_GT, ">>", idx, idx + 2)
            elif ch == "=":
                tok = lint.Tok(lint.TT.EQ, "=", idx, idx + 1)
                if chk_nxt_ch("="):
                    tok = lint.Tok(lint.TT.EQEQ, "==", idx, idx + 2)
            elif ch == "!":
                tok = lint.Tok(lint.TT.EXCLM, "!", idx, idx + 1)
                if chk_nxt_ch("="):
                    tok = lint.Tok(lint.TT.NOTEQ, "!=", idx, idx + 2)
            elif ch in lint.DIGITS:
                tok = self._get_num(src, src_len, idx)
            elif ch == "\"":
                tok = self._get_str(src, src_len, idx)
            elif ch in lint.VALID_WD_START_CHS:
                tok = self._get_wd(src, src_len, idx)
            else:
                tok = lint.Tok(lint.TT.INV, ch, idx, idx + 1)

            all_toks.append(tok)
            idx = tok.end
            idx = self._skip_ws(src, src_len, idx)

        return all_toks
