# coding: utf-8

# sympy.ntheory.generate.randprime(a, b)
# Return a random prime number in the range [a, b).
# pow(x, y[, z]) Python built-in function

from sympy.ntheory.generate import randprime
from sympy import numbers
from abc import ABC, abstractmethod

class CryptoSystem(ABC):
    """
    Classe abstraite d'un cryptosysteme
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self, m):
        raise NotImplementedError()

    @abstractmethod
    def decrypt(self, m):
        raise NotImplementedError()

    # génère un nombre premier de k bits exactement
    def getprime(self, k):
        p = randprime(2**(k-1), 2**k)
        return p

    # calcule un inverse x de a modulo n (0 < x < n)
    def invmod(self, a, n):
        t = numbers.igcdex(a, n)
        if t[2] != 1:
            raise Exception('Arguments must be relatively prime')

        return t[0] % n

    def are_relatively_prime(a, b):
        """Return ``True`` if ``a`` and ``b`` are two relatively prime numbers.
        Two numbers are relatively prime if they share no common factors,
        i.e. there is no integer (except 1) that divides both.
        """
        for n in range(2, min(a, b) + 1):
            if a % n == b % n == 0:
                return False
        return True
