#!/usr/bin/python3
# coding: utf-8

from paillier import Paillier
from votesystem import VoteSystem
from utils.ascii import get_ascii

def test_votesystem():
    # Paillier
    nbBits = 17
    paillier = Paillier(nbBits)

    # Vote system
    votesystem = VoteSystem(paillier)

    votesystem.vote('pour')
    votesystem.vote('contre')
    votesystem.vote('pour')
    votesystem.vote('pour')
    votesystem.vote('contre')
    votesystem.vote('against')
    votesystem.vote('pour')
    votesystem.vote('oui')
    votesystem.vote('pour')
    votesystem.vote('non')
    votesystem.vote('contre')
    votesystem.vote('contre')
    votesystem.vote('contre')
    votesystem.vote('pour')

    votesystem.count()

def test_paillier():
    nbBits = 17

    alice = Paillier(nbBits)
    bob = Paillier(nbBits)

    total = 1

    total *= bob.encrypt(10)
    total *= bob.encrypt(20)
    print(total)
    print(bob.decrypt(total))

    total = 1

    total *= bob.encrypt(30)
    print(total)
    print(bob.decrypt(total))


def main():
    x = 2
    y = 4


    """
    Alice et bob, deux utilisateur de Paillier.
    Alice ne connait rien
    Bob connait ex et ey
    """

    nbBits = 17
    alice = Paillier(nbBits)
    bob = Paillier(nbBits)

    # TODO changer de position ce bout de code
    ex = alice.encrypt(x)
    ey = alice.encrypt(y)

    """
    Bob choisit deux nombres aléatoires r et s
    Bob va ajouter à ex l'encryption de r
    Idem pour ey et s
    """

    r = 6
    s = 8

    er = alice.encrypt(r)
    es = alice.encrypt(s)

    # Propriétés homomorphiques de Paillier
    e1 = ex * er
    e2 = ey * es


    """
    On a donc e1 = [(x + r)] et e2 = [(y + s)].
    Bob va envoyer les deux à Alice
    """

    """
    Alice reçoit e1 et e2
    """

    d1 = int(alice.decrypt(e1))
    d2 = int(alice.decrypt(e2))

    d3 = d1 * d2

    e3 = bob.encrypt(d3)

    """
    Alice renvoit alors l'encryption du produit à bob (e3)
    Bob reçoit l'encryption d'Alice
    Il doit donc soustraire à cela [xs], [ry] et [rs]
    """

    # [xs]
    e4 = ex * es

    # [ry]
    e5 = er * ey

    # [rs]
    e6 = er * es

    d3 = bob.decrypt(e3)

    # This is magic !
    d3 -= x*s + r*y + r*s

    print(d3)

if __name__ == "__main__":
    main()
