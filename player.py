from .outcome import Outcome
from .wheel import Wheel
from .table import Table
from .bet import Bet

# this will act as a superclass to individual player types.
class Player(object):
    ''' Player Class
    Places bets on Outcomes, updates the stake with amounts won and lost.
    Uses Table to place bets on Outcomes; used by Game to record wins and losses.
    '''
    def __init__(self):
        pass
    
    def placeBets(self):
        '''Updates the Table with the various bets. This version creates a Bet instance from the black Outcome. 
        It uses Table placeBet() to place that bet.'''
        pass
    
    def win(self, bet):
        '''Notification from the Game that the Bet was a winner. 
        The amount of money won is available via the
        winAmount() method of theBet.'''
        pass
    
    def lose(self, bet):
        '''Notification from the Game that the Bet was a loser.'''
        pass


class Passenger57(object):
    '''Passenger57 constructs a Bet based on the Outcome named "Black". A player with a 1-track mind.'''
    
    def __init__(self, table=Table(), wheel=Wheel()):
        '''Constructs the Player with a specific table for placing bets. 
        This also creates the “black” Outcome. 
        This is saved in a variable named Passenger57.black for use in creating bets.
        '''
        # by querying the wheel
        #self.black = Wheel().getOutcome('Black')
        self.black = Outcome('Black', 1)
        self.wheel = wheel
        self.table = table

    def placeBets(self):
        '''Updates the Table with the various bets. This version creates a Bet instance from the black Outcome. 
        It uses Table placeBet() to place that bet.'''
        onBlack = Bet(amount=1, self.black)
        self.table.placeBet(onBlack)

    
    def win(self, bet):
        '''Notification from the Game that the Bet was a winner. 
        The amount of money won is available via the
        winAmount() method of the Bet.'''
        return f'Bet wins {bet.winAmount()}.'
    
    def lose(self, bet):
        '''Notification from the Game that the Bet was a loser.'''
        return 'Bet loses.'