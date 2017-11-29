    
class Outcome(object):
    ''' Outcome
    Responsibilities.
        A name for the bet and the payout odds. This isolates the calculation of the payout amount. Example: “Red”, “1”.
    Collaborators.
        - Collected by Wheel into the bins that reflect the bets that win;
        - collected by Table into the available bets for the    Player;
        - used by Game to compute the amount won from the amount that was bet.
    '''
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds


    def __eq__(self, other):
        '''Test Equality of the name attributes of self and other.'''
        return self.name == other.name


    def __ne__(self, other):
        '''Test Inequality of the name attributes of self and other.'''
        return self.name != other.name 


    def __hash__(self):
        '''Hash value for this outcome.'''
        return hash(self.name)


    def __str__(self):
        '''Easy-to-Read representation of outcome'''
        return '{name:s} ({odds:d}:1)'.format_map(vars(self))


    def __repr__(self):
        '''Detailed representation of this outcome.'''
        return '<Outcome "{name:s}" {odds:d}:1>'.format_map(vars(self))

    
    def winAmount(self, amount):
        '''Multiply this Outcome‘s odds by the given amount.
        The product is returned.'''
        return self.odds * amount


class PrisonOutcome(Outcome):
    '''subclass of Outcome, to cater for the en-prison rule in European Casinos :
    all losing bets are split ; only half the money is lost, the other half is termed a “push” and is returned to the player.'''
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def loseAmount(self, amount):
        pass
    
