import sys


class StyleObj:
    """
    Style object to apply formatting to text objects.
    """
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    red_4 = "\x1b[31m"
    green_4 = "\x1b[32m"
    yellow_4 = "\x1b[33m"
    blue_4 = "\x1b[34m"
    magenta_4 = "\x1b[35m"
    cyan_4 = "\x1b[36m"

    green_bg_8 = "\x1b[48;5;22m"
    magenta_bg_8 = "\x1b[48;5;55m"
    white_bg_8 = "\x1b[48;5;248m"
    black_fg_8 = "\x1b[38;5;0m"

    def fmt(self, string: str, *args: str) -> str:
        return ("".join(args) + string + self.reset)


def write(*msg: str, sep: str = " ", end: str = "\n") -> None:
    sys.stdout.write(sep.join(msg) + end)


def err(*msg: str, sep: str = " ", end: str = "\n") -> None:
    sys.stderr.write(S.fmt("E:", S.bold, S.red_4) + " " + sep.join(msg) + end)




def ljust(string: str, amt: int) -> str:
    return string.ljust(amt + len(string) - len(rm_ansi("", string)))


def rjust(string: str, amt: int) -> str:
    return string.rjust(amt + len(string) - len(rm_ansi("", string)))


S = StyleObj()
