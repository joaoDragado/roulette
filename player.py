from .bet import Bet

# this will act as a superclass to individual player types.
class Player(object):
    ''' Player Class
    Places bets on Outcomes, updates the stake with amounts won and lost.
    Uses Table to place bets on Outcomes; used by Game to record wins and losses.
    '''
    def __init__(self, table=None, stake=100, roundsToGo=100):
        '''Constructs the Player with a specific Table for placing Bets.
        stake : The player’s current stake. Initialized to the player’s starting budget.
        roundsToGo : Initialized by the overall simulation control to the maximum number of rounds to play.
        active : indicates whether player is playing ; defaults to True.
        cash_out : indicates that player exits simulation.
        '''
        self.table = table
        self.stake = stake
        self.roundsToGo = roundsToGo
        self.active = True
        self.cash_out = False

    def setRounds(self, roundsToGo):
        '''Sets the total number of rounds for the players run.'''
        self.roundsToGo = roundsToGo

    def setStake(self, amount):
        '''Set the initial stake of the player'''
        self.stake = amount

    def playing(self):
        '''checks player status : returns boolean if player can continue.'''
        return self.active & (not self.cash_out) & (self.stake >= self.table.minimum)

    def set_bet(self):
        '''picks the next bet that the player wages on.'''
        pass

    def check_bet(self, bet):
        '''checks that the bet complies with table limits & is within players stake.'''
        return (bet.amount <= self.stake) & self.table.isValid(bet)

    def placeBets(self):
        '''Updates the Table with the various bets. This version creates a Bet instance from the black Outcome.
        It uses Table placeBet() to place that bet.'''
        # check the simulation is not over
        if self.roundsToGo <= 0:
            self.cash_out = True
        # participate in roulette round
        self.roundsToGo -= 1
        # check player status
        if not self.playing():
            return
        # fetch bet
        bet = self.set_bet()
        # check bet eligibility ; if bet not compliant, exit
        if not self.check_bet(bet):
            return
        # place bet on roulette table
        self.table.placeBet(bet)
        # remove wager from players stake.
        self.stake -= bet.amount

    def win(self, bet):
        '''Called by Game.cycle when the player won
        the bet. Calculate amount won (via the
        winAmount() method of theBet) & 
        update players stake.'''
        self.stake += bet.winAmount()
        self.after_win(bet)

    def lose(self, bet):
        '''Placeholder method. the amount wagered was deducted from players stake when bet was placed.'''
        self.after_loss(bet)

    def after_win(self, bet):
        '''action to perform when player wins.'''
        pass

    def after_loss(self, bet):
        '''action to perform when player losses.'''
        pass


class Passenger57(Player):
    '''Passenger57 constructs a Bet based on the Outcome named "Black". A player with a 1-track mind.'''

    bet_amount = 1

    def __init__(self, **kwargs):
        '''Constructs the Player with a specific table for placing bets.
        Sets up container lists to record wins & losses. '''
        super().__init__(**kwargs)
        # by querying the wheel
        self.black = self.table.wheel.getOutcome('Black')
        self.wins = list()
        self.losses = list()

    def set_bet(self):
        '''Passenger57 always places the same bet on black.'''
        return Bet(self.bet_amount, self.black)

    def after_win(self, bet):
        '''appends winning amount to self.wins'''
        self.wins.append(bet.winAmount())

    def after_loss(self, bet):
        '''appends losing amount to self.losses'''
        self.losses.append(bet.amount)


class Martingale(Player):
    '''Martingale subclass of Player ; 
    employs the betting strategy of :
    doubling their bet on every loss, and 
    reseting their bet to a base amount on each win.'''

    bet_amount = 1

    def __init__(self, **kwargs):
        '''lossCount : losses counter ; the times to double the bet.
        betMultiple : the bet multiplier ; starts at 1,  doubled in each loss ; reset to 1 on each win. 
        This is always equal to 2^(lossCount) .'''
        super().__init__(**kwargs)
        self.black = self.table.wheel.getOutcome('Black')
        self.lossCount = 0
        # this is easier to exist inside set_bet
        #self.betMultiple = 2**(self.lossCount)

    def set_bet(self):
        '''always bets on black, the amount determined by the lossCount'''
        running_amount = (2**(self.lossCount)) * self.bet_amount 
        return Bet(running_amount, self.black)

    def after_win(self, _):
        '''reset lossCount to 1'''
        self.lossCount = 1

        
    def after_loss(self, _):
        '''increase lossCount by 1'''
        self.lossCount += 1
