import random as ran
import string

def gen_ran_strs(min_len: int = 100, max_len: int = 200):
    len_ = ran.randint(min_len, max_len)
    chs = string.ascii_letters + string.digits + string.punctuation
    return ''.join(ran.choice(chs) for _ in range(len_))

def gen_strs(min_len: int = 100, max_len: int = 200, cnt: int = 1000):
    tmp = [gen_ran_strs(min_len, max_len) for _ in range(cnt)]
    return tmp
