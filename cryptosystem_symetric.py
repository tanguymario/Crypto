from cryptosystem import CryptoSystem

class CryptoSystemSymetric(CryptoSystem):
    def __init__(self):
        pass

    def encrypt(self, m):
        raise NotImplementedError()

    def decrypt(self, m):
        raise NotImplementedError()
