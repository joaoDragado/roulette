import random
from bin import Bin
from binBuilder import BinBuilder

class Wheel(object):
    ''' Wheel Class
    Responsibilities.
    - Contains the 38 individual Bin instances as a tuple of 38 elements.
    - Uses a random number generator to simulate the spin of the roulette wheel;

    Collaborators.
    - Calls BinBuilder to construct the 38 bins.
    - used by the overall Game to get a next set of winning Outcomes.
    '''
    def __init__(self, rng=None, seed=None):
        '''instatiate the wheel bin;
           provide the option of setting a seed for the random generator;
           the arg seed=None seeds from current time.'''
        self.bins = {i:Bin() for i in range(38)}
        if rng is None:
            rng = random.Random()
            rng.seed(seed)
        self.rng = rng
        '''container for all possible outcomes.
        There are 152 discrete outcomes.'''
        self.all_outcomes = {}
        # the call below has been moved to create_wheel
        #BinBuilder().buildBins(self)
   

    def addOutcome(self, number, outcome):
        '''Adds the given Outcome : 
        to the Bin with the given number,
        to the all_outcomes container.'''
        self.bins[number] |= frozenset([outcome])
        self.all_outcomes[outcome.name] = outcome


    def getOutcome(self, name):
        '''obtain all possible outcomes based on their name ; name can be either str ot int type.
        returns a set of outocomes'''
        #possibles = [o for o in self.all_outcomes if #o.name == name]
        #return possibles[0]
        return self.all_outcomes[name]


    def next(self):
        '''Generates a random number between 0 and 37, and returns the randomly selected Bin'''
        return self.rng.choice(self.bins)


    def get(self, bin):
        '''Returns the given Bin from the internal collection.'''
        return self.bins[bin]
    
def create_wheel(rng=None, seed=None):
    '''function that acts as a wheel constructor; options to provide random generator, as well as seed value.
    function calls BinBuilder, and returns a fully populated wheel.'''
    wheel = Wheel(rng=rng, seed=seed)
    BinBuilder().buildBins(wheel)
    return wheel

    

