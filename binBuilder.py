
class binBuilder(object):
    '''class that generates the roulette bins
    and populates them with their corresponding
    outcomes.'''
    def __init__(self):
        pass
        
    def buildBins(self, wheel):
        '''Creates the Outcome instances and 
        uses the addOutcome() method to place 
        each Outcome in the appropropriate 
        Bin of wheel .'''
        pass
    
    def gen_straight_bets(self, wheel):
        '''generates straight bets.'''
        pass

    def gen_split_bets(self, wheel):
        '''generates split bets.'''
        pass
    
    def gen_street_bets(self, wheel):
        '''generates street bets.'''
        pass

    def gen_corner_bets(self, wheel):
        '''generates corner bets.'''
        pass

    def gen_line_bets(self, wheel):
        '''generates line bets.'''
        pass

    def gen_dozen_bets(self, wheel):
        '''generates dozen bets.'''
        pass

    def gen_column_bets(self, wheel):
        '''generates column bets.'''
        pass

    def gen_even_money_bets(self, wheel):
        '''generates even money bets 
        (red, black, odd, even, high, low).'''
        pass

    def gen_zeros_bets(self, wheel):
        '''generates the bets associated with
        the zero and double zero bins.'''
        pass
