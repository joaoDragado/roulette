

class Table(object):
    '''
    Table contains all the Bet s created by the Player. 
    Table has a betting minimum foe ach bet ; 
    Table also has a betting limit, and the sum of all of a player’s bets must be less than or equal to this limit. We assume a single Player in the simulation.

    We will want to segregate validation as a separate method, or sequence of methods. This is used by the Game just prior to spinning the wheel 
    '''
    def __init__(self, minimum=0, limit=0 ):
        # container for all bets
        self.bets = []
        self.minimum = minimum
        self.limit = limit
    
    def placeBet(self, bet):
        '''Adds this bet to the list of working bets.
        Should incorporate a try/except block to
        evaluate bet on table limits.'''
        self.bets.append(bet)

    def __iter__(self):
        '''Returns an iterator over the available list of Bet instances using a copy of the table's bets, via self.bets[:]'''
        pass

    def __str__(self):
        '''Return an easy-to-read string representation of all current bets.'''
        pass

    def __repr__(self):
        '''Return a representation of the form Table( bet, bet, ... ).'''
        pass
    
    def isValid(self):
        '''Raises an InvalidBet exception if the bets don’t pass the table limit rules, ensuring that :
        - The sum of all bets is less than or equal to the table limit.
        - All bet amounts are greater than or equal to the table minimum.'''
        pass