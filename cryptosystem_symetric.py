from cryptosystem import CryptoSystem

class CryptoSystemSymetric(CryptoSystem):
    def encrypt(self, m):
        raise NotImplementedError()

    def decrypt(self, m):
        raise NotImplementedError()
    

    def __init__(self):
        pass
