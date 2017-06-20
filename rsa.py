from cryptosystem_asymetric import CryptoSystemAsymetric

class RSA(CryptoSystemAsymetric):
    def __init__(self):
        super().__init__()
        self.generatekeys()

    def generatekeys(self, k):
        super().generatekeys(k)

        # N : public
        p = self.getprime(k)
        q = self.getprime(k)

        N = p * q
        Phi = N - p - q + 1

        self.setkeys(N, Phi)

    # Encrypt 
    def encrypt(self, m):
        # TODO

    # Decrypt
    def decrypt(self, c):
        # TODO
