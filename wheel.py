import random
from .bin import Bin

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
        self.all_outcomes = set()
        
    

    def addOutcome(self, number, outcome):
        '''Adds the given Outcome : 
        to the Bin with the given number,
        to the all_outcomes container.'''
        self.bins[number] |= frozenset([outcome])
        self.all_outcomes.add(outcome)


    def next(self):
        '''Generates a random number between 0 and 37, and returns the randomly selected Bin'''
        return self.rng.choice(self.bins)


    def get(self, bin):
        '''Returns the given Bin from the internal collection.'''
        return self.bins[bin]
    

    

