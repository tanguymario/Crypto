# coding: utf-8

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

        N2 = self.paillier.N * self.paillier.N
        for i in range(3):
            self.T[i] = self.T[i] * V[i] % N2


    def reset(self):
        self.T = [1, 1, 1]


    def count(self):
        pro = self.paillier.decrypt(self.T[0])
        against = self.paillier.decrypt(self.T[1])
        white = self.paillier.decrypt(self.T[2])

        print 'Nombre de votes \'pour\'   : {0:d}'.format(pro)
        print 'Nombre de votes \'contre\' : {0:d}'.format(against)
        print 'Nombre de votes blancs   : {0:d}'.format(white)


    def __init__(self, paillier):
        self.paillier = paillier
        self.reset()
