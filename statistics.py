import math

class IntegerStatistics(list):
	"""docstring for IntegerStatistics"""
	def __init__(self, *args):
		super().__init__(*args)

	def mean(self):
		'''Computes the mean of the List of values.'''
		return sum(self)/len(self)

	def stdev(self):
		'''Computes the standard deviation of the List values.'''
		return math.sqrt( sum( (x - self.mean())**2 for x in self) / (len(self) -1) )

