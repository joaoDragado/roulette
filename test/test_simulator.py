import pytest
from simulator import Simulator
from game import create_game
from player import Passenger57
from non_rnd import Non_rnd

# 3 blacks, 2 reds, 1 black, 4 reds, 1 black, 1 red, 2 blacks, 1 red
mix = [2,3,4,5,2, 2,4,2,3,5, 3,5,2,4,2]


def test_simulator():
    game = create_game(rng=Non_rnd(mix))
    sim = Simulator(game, Passenger57, init_duration=5,
                    init_stake=10, samples=3)
    stakes = sim.session()
    assert stakes == [10,20,10,20,10,20]
    stakes = sim.session()
    assert stakes == [10,20,30,40,30,20]
    stakes = sim.session()
    assert stakes == [10,0]
     
def test_gather():
	game = create_game(rng=Non_rnd(mix))
	sim = Simulator(game, Passenger57, init_duration=5, init_stake=10, samples=3)
	sim.gather()
	assert sim.durations == [6,6,2]
	assert sim.maxima == [20,40,10]




