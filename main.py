#!/usr/bin/python2
# coding: utf-8

from paillier import Paillier
from votesystem import VoteSystem

def main():
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

if __name__ == "__main__":
    main()
