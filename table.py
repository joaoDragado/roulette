from .bet import InvalidBet
from .wheel import create_wheel

class Table(object):
    '''
    Table contains all the Bets created by the Player. 
    Table has a betting minimum foe ach bet ; 
    Table also has a betting limit, and the sum of all of a player’s bets must be less than or equal to this limit. We assume a single Player in the simulation.

    We will want to segregate validation as a separate method, or sequence of methods. This is used by the Game just prior to spinning the wheel 
    '''
    def __init__(self, minimum=0, limit=10000):
        # container for all bets
        self.bets = []
        self.minimum = minimum
        self.limit = limit

    def isValid(self, bet):
        '''Evaluates bet on house limits :
        - The sum of all bets is less than or equal to the table limit.
        - All bet amounts are greater than or equal to the table minimum.'''
        pot = bet.amount
        for i in self.bets:
            pot += i.amount
        return (self.minimum <= bet.amount ) & (pot <= self.limit )

    def placeBet(self, bet):
        '''Adds this bet to the list of working bets.
        Should incorporate a try/except block to
        evaluate bet on table limits.'''
        if not self.isValid(bet):
            raise InvalidBet()
        self.bets.append(bet)

    def __iter__(self):
        '''Returns an iterator object of a copy of the table's bets, via self.bets[:] ; 
        is implicitly called at the start of loops.'''
        self._it = self.bets[:]
        return iter(self._it)
        
    def __next__(self):
        '''The __next__() method returns the next value and is implicitly called at each loop increment.'''
        try:
            result = next(self._it)
        except IndexError:
            raise StopIteration
        return result


    def __str__(self):
        '''Return an easy-to-read string representation of all current bets.'''
        return ' | '.join(str(x) for x in self.bets)

    def __repr__(self):
        '''Return a representation of the form Table( bet, bet, ... ).'''
        return 'Table(' + ', '.join(str(x) for x in self.bets) + ')'


def create_table():
    '''fucntion that constructs a virtual roulette table, i.e. a roulette wheel with a betting table ; uses create_wheel from Wheel.'''
    wheel = create_wheel()
    table = Table(wheel)
    return table