from cryptosystem import CryptoSystem
from abc import ABC, abstractmethod

class CryptoSystemAsymetric(CryptoSystem, ABC):
    """
    Classe abstraite d'un cryptosysteme asymétrique
    """

    # In bits
    MIN_KEY_LENGTH = 4

    def __init__(self):
        self.pk = None
        self.sk = None

    @abstractmethod
    def encrypt(self, m):
        raise NotImplementedError()

    @abstractmethod
    def decrypt(self, m):
        raise NotImplementedError()

    def generatekeys(self, k):
        if k < self.MIN_KEY_LENGTH:
            raise Exception("Key must be longer!")

    def getpublickey(self):
        return self.pk

    def getsecretkey(self):
        return self.sk

    def setkeys(self, publickey, secretkey):
        self.pk = publickey
        self.sk = secretkey
