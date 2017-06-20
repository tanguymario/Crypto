#!/usr/bin/python2
# coding: utf-8

from cryptosystem_asymetric import CryptoSystemAsymetric
from sympy import gcd
from random import randint

# Return x to the power y; if z is present, return x to the power y, modulo z
# (computed more efficiently than pow(x, y) % z). The two-argument form pow(x, y)
# is equivalent to using the power operator: x**y.

# sympy.numbers.igcdex(a, b)
# Returns x, y, g such that g = x * a + y * b = gcd(a, b).
# If gcd(a, n) = 1, then igcdex(a, n)[0] is the inverse of a modulo n.

class Paillier(CryptoSystemAsymetric):
    """
    Classe de Paillier
    """

    def __init__(self, nbBits):
        self.generatekeys(nbBits)

    # génére la clé publique N et la privée Phi
    def generatekeys(self, k):
        # N : public
        p = self.getprime(k)
        q = self.getprime(k)

        N = p * q
        Phi = N - p - q + 1

        self.setkeys(N, Phi)

    # Encrypt paillier
    def encrypt(self, m):
        if m < 0 or m > self.pk:
            raise Exception('m bad argument exception')

        # Trouver r tel que :
        #    - 0 < R < N
        #    - g = x * a + y * b = gcd(a, b)
        #      If gcd(a, n) = 1, then igcdex(a, n)[0] is the inverse of a modulo n.
        r = randint(1, self.pk - 1)
        while gcd(r, self.pk) != 1:
            r = randint(1, self.pk - 1)

        pk2 = self.pk * self.pk
        c = (pow(1 + self.pk, m, pk2) * pow(r, self.pk, pk2)) % pk2

        return c

    # Decrypt paillier
    def decrypt(self, c):
        # mu est l'inverse de N modulo Phi
        mu = self.invmod(self.pk, self.sk)

        r = pow(c, mu, self.pk)

        # s est l'inverse de r modulo N
        s = self.invmod(r, self.pk)
        pk2 = self.pk * self.pk
        m = ((c * pow(s, self.pk, pk2)) % pk2 - 1) / self.pk

        return m
