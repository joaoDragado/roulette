from .bet import Bet


class Player1236State(object):
	'''Player1326State is the superclass for all of the states in the 1-3-2-6 betting system.'''

	def __init__(self, player):
		'''The constructor for this class saves the Player1326 which will be used to provide the Outcome on which
		we will bet.'''
		self.player = player

	def currentBet(self):
		'''Constructs a new Bet from the player’s preferred Outcome. Each subclass has a different multiplier used when creating this Bet.'''
		pass

	def nextWon(self):
		'''Constructs the new Player1326State instance to be used when the bet was a winner.'''
		pass

	def nextLost(self):
		'''Constructs the new Player1326State instance to be used when the bet was a loser. 
		This method is the same for each subclass: it creates a new instance of Player1326NoWins.'''
		return Player1236NoWins(self.player) 


class Player1236NoWins(Player1236State):
	'''Player1326NoWins defines the bet and state transition rules in the 1-3-2-6 betting system. When there are no wins, the base bet value of 1 is used.'''

	def currentBet(self):
		'''Constructs a new Bet from the player’s outcome information. The bet multiplier is 1.'''
		return Bet(self.player.bet_amount, self.player.outcome)

	def nextWon(self):
		'''Constructs the new Player1326OneWin instance to be used when the bet was a winner.'''
		return Player1236OneWin(self.player) 


class Player1236OneWin(Player1236State):
	'''Player1326NoWins defines the bet and state transition rules in the 1-3-2-6 betting system. When there is 1 win.'''

	def currentBet(self):
		'''Constructs a new Bet from the player’s outcome information. The bet multiplier is 3.'''
		return Bet(3*self.player.bet_amount, self.player.outcome)

	def nextWon(self):
		'''Constructs the new Player1326TwoWins instance to be used when the bet was a winner.'''
		return Player1236TwoWins(self.player) 


class Player1236TwoWins(Player1236State):
	'''Player1326NoWins defines the bet and state transition rules in the 1-3-2-6 betting system. When there are 2 consecutive wins.'''

	def currentBet(self):
		'''Constructs a new Bet from the player’s outcome information. The bet multiplier is 2.'''
		return Bet(2*self.player.bet_amount, self.player.outcome)

	def nextWon(self):
		'''Constructs the new Player1326ThreeWins instance to be used when the bet was a winner.'''
		return Player1236ThreeWins(self.player) 


class Player1236ThreeWins(Player1236State):
	'''Player1326NoWins defines the bet and state transition rules in the 1-3-2-6 betting system. When there are 3 consecutive wins.'''

	def currentBet(self):
		'''Constructs a new Bet from the player’s outcome information. The bet multiplier is 6.'''
		return Bet(6*self.player.bet_amount, self.player.outcome)

	def nextWon(self):
		'''Constructs the new Player1326NoWins instance to be used when the bet was a winner.
		Essentially, the system is reset to the initial state.'''
		return Player1236NoWins(self.player) 

