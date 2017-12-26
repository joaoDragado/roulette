import random
from bet import Bet

# this will act as a superclass to individual player types.
class Player(object):
    ''' Player Class
    Places bets on Outcomes, updates the stake with amounts won and lost.
    Uses Table to place bets on Outcomes; used by Game to record wins and losses.
    '''
    def __init__(self, table=None, stake=100, roundsToGo=100, bet_amount=10):
        '''Constructs the Player with a specific Table for placing Bets.
        stake : The player’s current stake. Initialized to the player’s starting budget.
        roundsToGo : Initialized by the overall simulation control to the maximum number of rounds to play.
        active : indicates whether player is playing ; defaults to True.
        cash_out : indicates that player exits simulation.
        '''
        self.table = table
        self.stake = stake
        self.roundsToGo = roundsToGo
        self.bet_amount = bet_amount
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
        if self.roundsToGo < 1:
            self.cash_out = True
        #    self.active = False
        # participate in roulette round
        self.roundsToGo -= 1
        # check player status
        if self.cash_out:
            return
        # fetch bet
        bet = self.set_bet()
        # check bet eligibility ; if bet not compliant, exit
        if bet:
            if not self.check_bet(bet):
                self.active = False 
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

    def winners(self, outcomes):
        '''The set of Outcome instances that are part of the current win. Overriden by certain sublasses.'''
        pass


class Passenger57(Player):
    '''Passenger57 constructs a Bet based on the Outcome named "Black". A player with a 1-track mind.'''


    def __init__(self, **kwargs):
        '''Constructs the Player with a specific table for placing bets.
        Sets up container lists to record wins & losses. '''
        super().__init__(**kwargs)
        # by querying the wheel
        self._black = self.table.wheel.getOutcome('Black')
        self.wins = list()
        self.losses = list()

    def set_bet(self):
        '''Passenger57 always places the same bet on black.'''
        return Bet(self.bet_amount, self._black)

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

    
    def __init__(self, **kwargs):
        '''lossCount : losses counter ; the times to double the bet.
        betMultiple : the bet multiplier ; starts at 1,  doubled in each loss ; reset to 1 on each win. 
        This is always equal to 2^(lossCount) .'''
        super().__init__(**kwargs)
        self._black = self.table.wheel.getOutcome('Black')
        self.lossCount = 0
        # this is easier to exist inside set_bet
        #self.betMultiple = 2**(self.lossCount)

    def set_bet(self):
        '''always bets on black, the amount determined by the lossCount'''
        running_amount = (2**(self.lossCount)) * self.bet_amount 
        return Bet(running_amount, self._black)

    def after_win(self, _):
        '''reset lossCount to 0'''
        self.lossCount = 0

        
    def after_loss(self, _):
        '''increase lossCount by 1'''
        self.lossCount += 1


class SevenReds(Martingale):
    '''SevenReds is a Martingale player who places bets in Roulette. 
    This player waits until the wheel has spun red seven times in a row before betting black.'''
    
    def __init__(self, **kwargs):
        '''redCount : The number of reds yet to go. This starts at 7 , is reset to 7 on each non-red outcome, and decrements by 1 on each red outcome.'''
        super().__init__(**kwargs)
        self.redCount = 7
        self._red = self.table.wheel.getOutcome('Red')
        self._black = self.table.wheel.getOutcome('Black')

    def winners(self,outcomes):
        '''The game will notify a player of each spin using this method. This will be invoked even if the player places no bets.'''
        if self._red in outcomes:
            self.redCount -= 1
        else:
            self.redCount = 7

    def set_bet(self):
        '''If redCount is zero, this places a bet on black, using the bet multiplier.'''
        if self.redCount <= 0 :
            running_amount = (2**(self.lossCount)) * self.bet_amount 
            return Bet(running_amount, self._black)

        
class PlayerRandom(Player):
    '''PlayerRandom is a subclass of Player who places bets in Roulette. This player makes random bets around the layout.'''

    def __init__(self, rng=None, seed=None, **kwargs):
        '''Inherits all arguments for Player superclass.
        Includes a random generator argument purely for mock testing purposes, identical to the one in the Wheel class.'''
        if rng is None:
            rng = random.Random()
            rng.seed(seed)
        self.rng = rng
        super().__init__(**kwargs)
        

    def set_bet(self):
        '''choose at random 1 outcome out of all 152 discrete outcomes.
        These are located in the dict wheel.all_outcomes in the form of the structure OutcomeName : Outcome.
        We obtain the outcomes by calling the iterator dict.values and wrapping it in a list for random.choice.
        We then set & return the Bet.'''
        rnd_outcome = self.rng.choice(list(self.table.wheel.all_outcomes.values()))
        return Bet(self.bet_amount, rnd_outcome)


class Player1236(Player):
    '''Player1326 follows the 1-3-2-6 betting system. The player has a preferred Outcome (any even money bet - e.g. High).
    The amount wagered stems from the current betting state.
    The possible states are :
    
    Current state   Multiplier   On Win         On Loss
    ---------------------------------------------------
    No Wins         1            One Win        No Wins
    One Win         3            Two Wins       No Wins
    Two Wins        2            Three Wins     No Wins
    Three Wins      6            No Wins        No Wins
    
    The multiplier is always applied to the initial bet amount.
    '''
    def __init__(self, **kwargs):
        from player1236 import Player1326NoWins 
        '''Initializes the state and the outcome. 
        The state is set to the initial state of an instance of Player1326NoWins.
        The outcome is set to some even money proposition, e.g. "High".'''
        super().__init__(**kwargs)
        self.outcome = self.table.wheel.getOutcome('High')
        self.state = Player1326NoWins(self)

    def set_bet(self):
        '''Updates the Table with a bet created by the current state. 
        This method delegates the bet creation to state object’s currentBet() method.'''
        return self.state.currentBet()

    def after_win(self, _):
        '''Uses the superclass method to update the stake with an amount won. 
        Uses the current state to determine what 
        the next state will be (by calling state‘s objects nextWon() method ) and 
        saving the new state in state.'''
        self.state = self.state.nextWon()

        
    def after_loss(self, _):
        '''Uses the current state to determine what the next state will be. 
        This method delegates the next state decision to state object’s nextLost() method, saving the result in state.'''
        self.state = self.state.nextLost()

        
        


def create_player(player_class, table, stake=100, duration=100, bet_amount=10):
    '''Create a new player of a particular class of betting strategy.
    If player_class defined as string, use the commented code below :
    '''
    #player_class_name = globals()[player_class]
    #player = player_class_name(table=table)
    player = player_class(table=table, bet_amount=bet_amount)
    player.setRounds(duration)
    player.setStake(stake)
    return player
