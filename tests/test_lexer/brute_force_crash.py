#!/usr/bin/env -S python3 -BOO
import lexer.eng as leng
import tests.test_lexer.gen_rand_strs as gen_rand_strs

x = leng.Lexer()
y = gen_rand_strs.gen_strs(min_len=10000, max_len=20000, cnt=100)
for i in y:
    print(x.lex(i))
