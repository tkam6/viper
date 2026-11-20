#!/usr/bin/env -S python3 -BOO
import os
import stat
import sys
import typing as ty

from src.lexer import eng as leng
from src.parser import eng as peng
from src.utils import consts as uconst
from src.utils import debug as udeb
from src.utils import err_codes as uerr
from src.utils import gen as ugen


def parse_argv(
    raw_argv: list[str],
    min_args: int,
    max_args: int,
    valid_opts: tuple[str],
    valid_flags: tuple[str],
) -> tuple[list[str], dict[str, str], list[str]] | ty.NoReturn:
    "Parse argv sent to main program"
    parse_opts_flags = True
    args, opts, flags = [], {}, []
    skip = 0    # Used to skip entries, like values of options

    for i, raw in enumerate(raw_argv):
        if skip:
            skip -= 1
            continue
        # Option and flag parsing disabled
        if not parse_opts_flags:
            args.append(raw)
            continue
        # `--` disables option and flag parsing
        if raw == "--":
            parse_opts_flags = False
            continue
        if raw.startswith("-"):
            if raw in valid_flags:
                flags.append(raw)
            elif raw in valid_opts:
                if i >= len(raw_argv) - 1:
                    ugen.err(f"Expected value for option '{raw}'")
                    sys.exit(uerr.RC_NO_VAL_OPT)
                opts[raw] = raw_argv[i + 1]
                skip += 1
            else:
                ugen.err(f"Invalid option/flag: '{raw}'")
                sys.exit(uerr.RC_INV_OPT_FLAG)
            continue
        args.append(raw)

    if len(args) < min_args:
        ugen.err(f"Argument underflow: {len(args)} not in [{min_args}, {max_args}]")
        sys.exit(uerr.RC_ARG_UNDERFLOW)
    elif len(args) > max_args:
        ugen.err(f"Argument overflow: {len(args)} not in [{min_args}, {max_args}]")
        sys.exit(uerr.RC_ARG_OVERFLOW)
    return (args, opts, flags)


def main() -> None:
    args, opts, flags = parse_argv(sys.argv[1 :], 0, 0, valid_opts=("-f", "--file"), valid_flags=())
    flnm = (opts.get("-f") or opts.get("--file")) or "/home/vallu/devel/viper/dev/main.vi"
    try:
        stat_res = os.stat(flnm)
        # Check if not regular file; directories, /dev/full and such sort eliminated
        if not stat.S_ISREG(stat_res.st_mode):
            ugen.err(f"Not a regular file: {repr(flnm)}")
            sys.exit(uerr.RC_NOT_REG_FL)
        # Check if input size exceeds max size
        if stat_res.st_size > uconst.MAX_INP_FLSZ:
            ugen.err(f"Input file too large ({repr(flnm)}): must be less than {uconst.MAX_INP_FLSZ}B")
            sys.exit(uerr.RC_INP_FL_TOO_LARGE)
        vi_fl = open(flnm)
        vi_fl.seek(0)
        # Currently reads whole file into memory
        # TODO: Change to stream from file
        src = vi_fl.read()
    except FileNotFoundError:
        ugen.err(f"No such file: {repr(flnm)}")
        sys.exit(uerr.RC_NO_FL)
    except PermissionError:
        ugen.err(f"Access denied: {repr(flnm)}")
        sys.exit(uerr.RC_NO_PERM)
    # Technically not needed as regular file check is already done before
    except IsADirectoryError:
        ugen.err(f"Is a directory: {repr(flnm)}")
        sys.exit(uerr.RC_IS_A_DIR)
    except OSError as e:
        ugen.err(f"OS error; {e.strerror}")
        sys.exit(uerr.RC_OS_ERR)
    except UnicodeDecodeError:
        ugen.err(f"Is not text: {repr(flnm)}")
        sys.exit(uerr.RC_CANT_DECODE)
    lexer = leng.Lexer()
    parser = peng.Parser()
    print(parser.parse(lexer.lex(src)))


if __name__ == "__main__":
    main()
