import pytest
from ..player import create_player, Passenger57
from ..wheel import create_wheel
from ..game import create_game
from ..non_rnd import Non_rnd


def test_roulette_game():
    game = create_game(rng=Non_rnd([0, 2]))
    player = create_player(Passenger57, game.table, 20, duration=10)

    game.cycle(player)
    assert player.losses == [10]
    assert player.wins == list()
    game.cycle(player)
    assert player.losses == [10]
    assert player.wins == [20]

