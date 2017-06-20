# coding: utf-8

# sympy.ntheory.generate.randprime(a, b)
# Return a random prime number in the range [a, b).
# pow(x, y[, z]) Python built-in function

from sympy.ntheory.generate import randprime
from sympy import numbers

class CryptoSystem:
    """
    Classe abstraite d'un cryptosysteme
    """

    def __init__(self):
        pass

    # calcule un inverse x de a modulo n (0 < x < n)
    def invmod(self, a, n):
        t = numbers.igcdex(a, n)
        if t[2] != 1:
            raise Exception('Arguments must be relatively prime')

        return t[0] % n

    def encrypt(self, m):
        raise NotImplementedError()

    def decrypt(self, m):
        raise NotImplementedError()

    # génère un nombre premier de k bits exactement
    def getprime(self, k):
        p = randprime(2**(k-1), 2**k)
        return p
