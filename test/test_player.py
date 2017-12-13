import pytest
from ..player import Passenger57, Martingale, create_player
from ..table import  Table, create_table
from ..wheel import  create_wheel
from ..non_rnd import Non_rnd
from ..game import Game, create_game

# all black sequence
blacks = [20,6,15,31,2,10]
# 2 black, 3 reds
mix_2b_3r = [11,29,3,9,27]
# all reds
reds = [21,7,9,21,]


def test_P57():
	game = create_game(rng=Non_rnd(mix_2b_3r))
	p57 = create_player(Passenger57, game.table, 100, 100)
	game.cycle(p57)
	game.cycle(p57)
	assert p57.stake == 102
	game.cycle(p57)
	game.cycle(p57)
	assert p57.stake == 100
	game.cycle(p57)
	assert p57.stake == 99

def test_Martingale():
	game = create_game(rng=Non_rnd(mix_2b_3r))
	mG = create_player(Martingale, game.table, 100, 100)
	game.cycle(mG)
	assert mG.stake == 101
	game.cycle(mG)
	assert mG.stake == 102
	game.cycle(mG)
	assert mG.stake == 101
	game.cycle(mG)
	assert mG.stake == 99
	game.cycle(mG)
	assert mG.stake == 95

