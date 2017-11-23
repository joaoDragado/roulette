


class Game(object):
    ''' Game manages the sequence of actions that defines the game of Roulette. 
    Game notifies Player to place Bets, spins Wheel, & resolves the Bets present on the Table.

    The final aim is to use this class to run simulations on betting strategies , play a finite number of games, and collect the final value of the Player‘s stake.
    '''
    def __init__(self, wheel, table):
        '''Constructs a new Game, using a given Wheel and Table.
        We utilize the Strategy design pattern ; 
        Each of these collaborating objects is  a replaceable strategy, and can be changed by the client that uses this game.'''
        pass
    
    def cycle(self, player):
        ''' 
        Executes a single cycle of play with a given Player. 
        1. call thePlayer‘s placeBets() method to get bets,
        2. call theWheel‘s next() method to get the next winning Bin, 
        3. call theTable‘s iterator to get an Iterator over the Bets. If the winning Bin contains the Outcome, call the thePlayer win() method otherwise call the thePlayer lose() method.
        '''
        pass
