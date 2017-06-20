#!/usr/bin/python2
# coding: utf-8

# Imports
from sympy.ntheory.generate import randprime
from sympy import numbers
from sympy import gcd
from random import randint

# sympy.ntheory.generate.randprime(a, b)
# Return a random prime number in the range [a, b).
# pow(x, y[, z]) Python built-in function

# Return x to the power y; if z is present, return x to the power y, modulo z
# (computed more efficiently than pow(x, y) % z). The two-argument form pow(x, y)
# is equivalent to using the power operator: x**y.

# sympy.numbers.igcdex(a, b)
# Returns x, y, g such that g = x * a + y * b = gcd(a, b).
# If gcd(a, n) = 1, then igcdex(a, n)[0] is the inverse of a modulo n.

class CryptoSystem:
    """
    Classe abstraite d'un cryptosysteme
    """

    # calcule un inverse x de a modulo n (0 < x < n)
    def invmod(self, a, n):
        t = numbers.igcdex(a, n)
        if t[2] != 1:
            raise Exception('Arguments must be relatively prime')

        return t[0] % n

    # génère un nombre premier de k bits exactement
    def getPrime(self, k):
        p = randprime(2**(k-1), 2**k)
        return p

    def __init__(self):
        pass


class Paillier(CryptoSystem):
    """
    Classe de Paillier
    """

    def getPublicKey(self):
        return self.N


    def getPrivateKey(self):
        return self.Phi


    # génére la clé publique N et la privée Phi
    def generateKeys(self, k):
        # N : public
        p = self.getPrime(k)
        q = self.getPrime(k)
        self.N = p * q

        # Phi = (p-1) * (q-1) : private
        self.Phi = self.N - p - q + 1

    # Encrypt paillier
    def encrypt(self, m):
        if m < 0 or m > self.N:
            raise Exception('m bad argument exception')

        # Trouver r tel que :
        #    - 0 < R < N
        #    - g = x * a + y * b = gcd(a, b)
        #      If gcd(a, n) = 1, then igcdex(a, n)[0] is the inverse of a modulo n.
        r = randint(1, self.N - 1)
        while gcd(r, self.N) != 1:
            r = randint(1, self.N - 1)

        N2 = self.N * self.N
        c = (pow(1 + self.N, m, N2) * pow(r, self.N, N2)) % N2
        return c

    # Decrypt paillier
    def decrypt(self, c):
        # mu est l'inverse de N modulo Phi
        mu = self.invmod(self.N, self.Phi)
        r = pow(c, mu, self.N)

        # s est l'inverse de r modulo N
        s = self.invmod(r, self.N)
        N2 = self.N * self.N
        m = ((c * pow(s, self.N, N2)) % N2 - 1) / self.N

        return m


    def __init__(self, nbBits):
        self.generateKeys(nbBits)

class VoteSystem:
    # Une ébauche de système de référendum (on comptabilise les 'pour',
    # les 'contre', et le reste est compté comme vote blanc.
    # * la fonction vote permet de chiffrer à un votant de chriffrer son vote
    #   (seul N est utilisé).
    # * la fonction addvote permet de comptabiliser un cours de vote,
    #   sans avoir à déchiffrer le total (seul N est utilisé)
    # * la
    def vote(self, v):
        if v == 'pour':
            V = [1, 0, 0]
        elif v == 'contre':
            V = [0, 1, 0]
        else: # vote blanc
            V = [0, 0, 1]

        V[0] = self.paillier.encrypt(V[0])
        V[1] = self.paillier.encrypt(V[1])
        V[2] = self.paillier.encrypt(V[2])

        self.addVote(V)

    def addVote(self, V):
        N2 = self.paillier.N * self.paillier.N
        for i in range(3):
            T[i] = T[i] * V[i] % N2

        return T

    def reset(self):
        T = [0, 0, 0]

    def count(self):
        pro = self.paillier.decrypt(T[0])
        against = self.paillier.decrypt(T[1])
        white = self.paillier.decrypt(T[2])

        print 'Nombre de votes \'pour\'   : {0:d}'.format(pro)
        print 'Nombre de votes \'contre\' : {0:d}'.format(against)
        print 'Nombre de votes blancs   : {0:d}'.format(white)


    def __init__(self, pailler):
        self.paillier = paillier


# print decrypt(encrypt(5, N) * encrypt(3, N) % (N*N), N, Phi)

# Paillier
nbBits = 17
paillier = Paillier(nbBits)

# Vote system
voteSys = VoteSystem(paillier)

T = [1, 1, 1]

V = voteSys.vote('pour')
V = voteSysvote('contre')
V = voteSysvote('pour')
V = voteSys.vote('pour')
V = voteSys.vote('contre')
V = voteSys.vote('against')
V = voteSys.vote('pour')
V = voteSys.vote('oui')
V = voteSys.vote('pour')
V = voteSys.vote('non')
V = voteSys.vote('contre')
V = voteSys.vote('contre')
V = voteSys.vote('contre')
V = voteSys.vote('pour')

voteSys.count()
