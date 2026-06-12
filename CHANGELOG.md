# CHANGELOG

## Latest commit

feat: semicolon, grouping symbols lexing

- `src/lexer/intl.py`
1. Added grouping symbols (parentheses, braces and brackets)
- `src/lexer/eng.py`
1. Grouped arithmetic symbols with a lookup table
2. Added lexing logic for grouping symbols
3. Added lexing logic for semicolon
- `pyproject.toml`
1. Touched and edited pyproject.toml

## Commit 8074c981e36c26bdc79738d913e3e8c5289645a1

fix: lexer; docs: commit guidelines; tests: lexer; feat: started parser

- `src/lexer/eng.py`: fixed several bugs; changed some token values; added in
string character escaping
- `dev/commit_msg_guidelns.txt`: added a commit message guideline file
- `tests/test_lexer/`: wrote brute force tests for lexer (not sure it's the
correct term for it)

## Commit 623c14758770cb531d21e7f4f8764249131ccef4

Wrote the lexer, main program.

- `src/lexer/eng.py`, `src/lexer/intl.py`: Wrote the lexer.
- `src/main.py`: Wrote the main program.

## Commit 34705ae06471c6a10ce8dcd73df4bec66b4d874e

Initial commit
