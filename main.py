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

    r = 6
    s = 8

    


if __name__ == "__main__":
    main()
