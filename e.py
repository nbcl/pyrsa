import os
from math import gcd

def crand(bytes_: int) -> int:
    """Returns system-specific randomly generated
    integer from urandom byte sequence
    """
    return int.from_bytes(os.urandom(bytes_), byteorder='big')

def gen_public_e(lambda_: int) -> int:
    """ Generates decrecingly smaller sequence of bytes and
    converts them to integer until one satisfies > lambda

    Continues with half the ammount of necesary bytes decreasing
    by one integer until gcd(candidate, lambda) == 1.
    """
    bytes_ = 1028 + 1

    candidate = crand(bytes_)
    while candidate > lambda_:  # Finds random amount of bytes 
        candidate = crand(bytes_)
        bytes_ -= 1

    candidate = crand(bytes_ // 2)  # Generates new candidate in the middle
    e = 2**16 + 1

    while candidate > e:  # Finds candidate that satisfies gcd
        if gcd(candidate, lambda_) == 1:
            break
        candidate -= 1
    return candidate
