def match(
    tok: lint.Tok,
    typ: lint.TT | None = None,
    val: lint.TT | None = None
) -> bool:
    if typ is not None and val is not None:
        return tok.typ == typ and tok.val == val
    elif typ is not None:
        return tok.typ == typ
    elif val is not None:
        return tok.val == val
    else:
        raise ValueError("Atleast one of typ or val must be non-None")
