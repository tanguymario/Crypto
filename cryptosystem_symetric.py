from cryptosystem import CryptoSystem
from abc import ABC, abstractmethod

class CryptoSystemSymetric(CryptoSystem, ABC):
    """
    Classe abstraite d'un cryptosysteme
    """

    def __init__(self):
        self.k = None

    @abstractmethod
    def encrypt(self, m):
        raise NotImplementedError()

    @abstractmethod
    def decrypt(self, m):
        raise NotImplementedError()

    def setkey(self, k):
        self.k = k
