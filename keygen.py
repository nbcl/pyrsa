from carmichael import pcar
from e import gen_public_e
import math

class keyGen():
    """Generates public and private RSA keys
    using p, q, λ(n), e, d parameters
    """
    def __init__(self):
        """Inits keyGen class 
        Calculates λ(n), e, d parameters
        """
        from primes import p, q
        n = p * q

        print('Generating RSA keys, 1028 bit long primes')
        lam = pcar(p, q)   # prime-variation of the Carmichael function
        printlog("λ(n)", lam)

        e = gen_public_e(lam)  # e part of the public key is chosen
        printlog("public", e)

        d = pow(e, -1, lam)  # d satiesfies e**-1 % lam(n)
        printlog("private", d)

        self.public = (n, e)
        self.private = (d)
    
def printlog(name: str, p: int):
    """ Terminal log printer function
    """
    first = str(p)[0:3]
    mid = str(len(str(p)))
    last = str(p)[-3:len(str(p))]
    print(name + " : " + first + " ... (" + mid + " more digits) ... " + last + "\n")
    
