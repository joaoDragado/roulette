
class Bet(object):
    '''Bet associates an amount and an Outcome, and also with the Player placing the Bet.'''
    def __init__(self, amount, outcome):
        self.amountBet = amount
        self.outcome = outcome
        

    def winAmount(self):
        '''returns the amount won, plus the original stake'''
        return self.amountBet * (self.outcome.odds + 1)
    
    # this method will become obsolete, since when a player places a bet, the amount will be deducted from his/her stake.
    def loseAmount(self):
        '''returns the amount lost, aka the original stake.'''
        return self.amountBet

    def __str__(self):
        '''A string representation of the bet in the form "amount on outcome".'''
        return '${} on {}'.format(self.amountBet, self.outcome)

    def __repr__(self):
        '''string representation of the bet in the form "Bet(amount, outcome)".'''
        return 'Bet({},{})'.format(self.amountBet, self.outcome)