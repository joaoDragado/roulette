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
reds = [21,7,9,21,27]


def test_P57():
	game = create_game(rng=Non_rnd(mix_2b_3r))
	p57 = create_player(Passenger57, game.table, 100, duration=10)
	game.cycle(p57)
	game.cycle(p57)
	assert p57.stake == 120
	game.cycle(p57)
	game.cycle(p57)
	assert p57.stake == 100
	game.cycle(p57)
	assert p57.stake == 90

def test_Martingale():
	game = create_game(rng=Non_rnd(mix_2b_3r))
	mG = create_player(Martingale, game.table, 100, 10)
	game.cycle(mG)
	assert mG.stake == 110
	game.cycle(mG)
	assert mG.stake == 120
	game.cycle(mG)
	assert mG.stake == 110
	game.cycle(mG)
	assert mG.stake == 90
	game.cycle(mG)
	assert mG.stake == 50

def test_martingale_lucky():
    # black, red, red,red, black, black
    rng = Non_rnd([2, 5, 9, 12, 11, 10])
    game = create_game(rng=rng)

    player = create_player(Martingale, game.table, 200, 10)
    # win
    game.cycle(player)
    assert player.stake == 210
    game.cycle(player)
    # loose, bet 10
    assert player.stake == 200
    game.cycle(player)
    # loose, bet 20
    assert player.stake == 180
    game.cycle(player)
    # loose, bet 40
    assert player.stake == 140
    game.cycle(player)
    # win , bet 80
    assert player.stake == 220
    game.cycle(player)
    # win, bet 10
    assert player.stake == 230
