from cryptosystem import CryptoSystem

class CryptoSystemAsymetric(CryptoSystem):
    def encrypt(self, m):
        raise NotImplementedError()

    def decrypt(self, m):
        raise NotImplementedError()

    def generatekeys(self):
        raise NotImplementedError()

    def setkeys(self, publickey, secretkey):
        self.pk = publickey
        self.sk = secretkey

    def getpublickey(self):
        return self.pk


    def getsecretkey(self):
        return self.sk


    def __init__(self):
        pass
