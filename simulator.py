from .player import create_player
from .wheel import create_wheel
from .table import Table
from .game import Game

class Simulator(object):
	'''Simulator exercises the Roulette simulation with a given Player placing bets. It reports raw statistics on a number
	of sessions of play.'''
	def __init__(self, game, player_class, init_duration=250, init_stake=100, samples=50):
		'''initDuration :Initial value for the duration of each session; i.e. the num of roulette spins.
		initStake : The stake value to use when initializing a Player for a session ; a count of the number of bets placed;
		samples : The number of game sessions to simulate.
		durations : A List of lengths of time the Player remained in the game. Each session of play produces a duration metric.
		maxima : A List of maximum stakes for each Player.
		player : The Player; essentially, the betting strategy we are simulating.
		game : The casino game we are simulating ;an instance of Game, which embodies the various rules, the Table and the Wheel. '''
		self.game = game
		self.player_class = player_class
		self.init_duration = init_duration
		self.init_stake = init_stake
		self.samples = samples
		self.durations = list()
		self.maxima = list()

	def session(self):
		'''Executes a single game session. 
		The Player is initialized. 
		An empty List of stake values is created. 
		The session loop executes until the Player playing() returns false.
		This loop executes the Game cycle(); then it gets the stake from the Player and appends this amount to the
		List of stake values. The List of individual stake values is returned as the result of the session of play'''
		stakes = list()
		player = create_player(self.player_class, self.game.table, self.init_stake, self.init_duration)
		print(f'Player playing status : {player.playing()}')
		while player.playing():
			stakes.append(player.stake)
			self.game.cycle(player)
		return stakes

	def gather(self):
		'''Executes self.samples of games sessions.
		Each game session returns a List of stake values.
		When the session is over (either the play reached their time limit or their stake was spent), then the length of the session List and the maximum value in the session List are the resulting duration and maximum metrics. 
		These two metrics are appended to the durations list and the maxima list.'''
		for i in range(self.samples):
			stakes = self.session()
			self.durations.append(len(stakes))
			self.maxima.append(max(stakes))
		# save output to respective tsv files
		# each line represent 1 simulation (the data from samples * sessions)
		with open('durations.tsv', 'at') as f:
		    f.write('\t'.join(str(i) for i in self.durations)+'\n')
		with open('maxima.tsv', 'at') as f:
		    f.write('\t'.join(str(i) for i in self.maxima)+'\n')

