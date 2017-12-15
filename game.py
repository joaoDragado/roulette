from .wheel import Wheel, create_wheel
from .table import Table


class Game(object):
    ''' Game manages the sequence of actions that defines the game of Roulette. 
    Game notifies Player to place Bets, spins Wheel, & resolves the Bets present on the Table.

    The final aim is to use this class to run simulations on betting strategies , play a finite number of games, and collect the final value of the Player‘s stake.
    '''
    def __init__(self, table):
        '''Constructs a new Game, using a given Wheel and Table.
        We utilize the Strategy design pattern ; 
        Each of these collaborating objects is  a replaceable strategy, and can be changed by the client that uses this game.'''
        self.table = table

    
    def cycle(self, player):
        ''' 
        Executes a single cycle of play with a given Player. 
        1. call thePlayer‘s placeBets() method to get bets,
        2. call theWheel‘s next() method to get the next winning Bin, 
        3. call theTable‘s iterator to get an Iterator over the Bets. If the winning Bin contains the Outcome, call the thePlayer win() method otherwise call the thePlayer lose() method.
        - the player.playing() is called twice , so that we follow the true life sequence of roulette events, while allowing for the wheel to spin even if the player is not participating.
        '''
        # check the simulation is not over
        if player.roundsToGo < 1:
            player.cash_out = True
        
        # if player inactive , exit
        if not player.playing():
            return
                # if player active, place bets
        if player.playing():
            player.placeBets()
            # spin the roulette wheel
        winningBin =  self.table.wheel.next()
        # iterate over all bets
        for bet in self.table:
            if bet.outcome in winningBin:
                player.win(bet)
            else:
                player.lose(bet)
        # clear table of all bets
        self.table.bets.clear()
        #player.roundsToGo -= 1

        
def create_game(rng=None, seed=None):
    '''creates a new roulette game , with its own Table-Wheel.
    the keyword arguments for random generator and seed value relate to the wheel. Returns a Game class object.'''
    wheel = create_wheel(rng=rng, seed=seed)
    table = Table(wheel)
    game = Game(table)
    return game
