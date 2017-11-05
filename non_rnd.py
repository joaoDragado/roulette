class Non_rnd(object):
    '''class that defines a non random generator, with elements provided by a given sequence (list)'''
    def __init__(self, seq, seed=None):
        self.seq = seq
        self.index = 0

    
    def choice(self):
        val = self.seq[self.index]
        self.index += 1
        return val
