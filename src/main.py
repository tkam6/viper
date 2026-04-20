#!/usr/bin/env -S python3 -BOO

import lexer.eng as leng
import utils.debug as udeb

vi_fl = open("/home/vallu/personal/viper/dev/main.vi", "a+")
vi_fl.seek(0)
src = vi_fl.read()
lxr = leng.Lexer()
udeb.pprn(lxr.lex(src))
