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
    def __init__(self, table, stake=100, spins=100):
        '''Constructs the Player with a specific Table for placing Bets.
        stake : The player’s current stake. Initialized to the player’s starting budget.
        spins : Initialized by the overall simulation control to the maximum number of rounds to play.
        active : indicates whether player is playing ; defaults to True.
        cash_out : indicates that player exits simulation.
        '''
        self.table = table
        self.stake = stake
        self.spins = spins
        self.active = True
        self.cash_out = False

    def set_spins(self, spins):
        '''Sets the total number of rounds for the player\s run.'''
        self.spins = spins

    def set_stake(self, amount):
        '''Set the initial stake of the player'''
        self.stake = amount

    def eligible(self):
        '''checks player eligibility : returns boolean if player can continue.'''
        return self.active & (not self.cash_out) & (self.stake > 0)

    def set_bet(self):
        '''picks the next bet that the player wages on.'''
        pass

    def check_bet(self, bet):
        '''checks that the bet complies with table limits & is within player\s stake.'''
        return (bet.amount <= self.stake) & self.table.isValid(bet) 

    def placeBets(self):
        '''Updates the Table with the various bets. This version creates a Bet instance from the black Outcome. 
        It uses Table placeBet() to place that bet.'''
        # check the simulation is not over
        if self.spins <= 0 :
            self.cash_out = True
        # participate in roulette round
        self.spins -= 1
        # check player eligibility
        if not self.eligible():
            return
        # fetch bet
        bet = self.set_bet()
        # check bet eligibility
        if self.check_bet(bet):
            # place bet on roulette table
            self.table.placeBet(bet)
            # remove wager from player\s stake.
            self.stake -= bet.amount
        else : 
            return

    def win(self, bet):
        '''Called by Game.cycle when the player won
        the bet. Calculate amount won (via the
        winAmount() method of theBet) & 
        update player\s stake.'''
        self.stake += bet.winAmount()
    
    def lose(self, bet):
        '''Placeholder method. the amount wagered was deducted from player\s stake when bet was placed.'''
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
        It uses Table.placeBet() to place that bet.'''
        onBlack = Bet(amount=1, outcome=self.black)
        self.table.placeBet(onBlack)

    
    def win(self, bet):
        '''Notification from the Game that the Bet was a winner. 
        The amount of money won is available via the
        winAmount() method of the Bet.'''
        return f'Bet wins {bet.winAmount()}.'
    
    def lose(self, bet):
        '''Notification from the Game that the Bet was a loser.'''
        return 'Bet loses.'