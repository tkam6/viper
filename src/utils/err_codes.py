iota_cntr = 0
def iota(set_val: int | None = None):
    global iota_cntr
    if set_val is not None:
        iota_cntr = set_val
    tmp = iota_cntr
    iota_cntr += 1
    return tmp


RC_ALL_GOOD = iota(0)
# General errors
RC_OS_ERR = iota()
RC_NOT_REG_FL = iota()
RC_INP_FL_TOO_LARGE = iota()

# argv parse errors
RC_ARG_UNDERFLOW = iota(10)
RC_ARG_OVERFLOW = iota()
RC_INV_OPT_FLAG = iota()
RC_NO_VAL_OPT = iota()

# Specific errors
RC_NO_FL = iota(100)
RC_IS_A_DIR = iota()
RC_NO_PERM = iota()
RC_CANT_DECODE = iota()
