import pytest
from outcome import Outcome
from wheel import Wheel
from binBuilder import BinBuilder

wheel = Wheel()
bb = BinBuilder()

def test_gen_bets():
    bb.gen_straight_bets(wheel)
    assert wheel.get(5) == frozenset([Outcome('5', 35)])
    assert len(wheel.all_outcomes) == 38

    #test_gen_split_bets():
    bb.gen_split_bets(wheel)
    assert len(wheel.get(8)) == 5
    assert len(wheel.get(23)) == 5
    assert len(wheel.get(2)) == 4
    assert len(wheel.get(34)) == 3
    assert len(wheel.all_outcomes) == 38 + 57

    #test_gen_street_bets():
    bb.gen_street_bets(wheel)
    assert len(wheel.get(9)) == 5
    assert len(wheel.get(23)) == 6
    assert len(wheel.get(31)) == 5
    assert len(wheel.all_outcomes) == 95 + 12

    #test_gen_corner_bets():
    bb.gen_corner_bets(wheel)
    assert len(wheel.get(3)) == 5
    assert len(wheel.get(9)) == 7
    assert len(wheel.get(23)) == 10
    assert len(wheel.get(31)) == 7
    assert len(wheel.get(35)) == 7
    assert len(wheel.all_outcomes) == 107 + 22

    #test_gen_line_bets():
    bb.gen_line_bets(wheel)
    assert len(wheel.get(3)) == 6
    assert len(wheel.get(9)) == 9
    assert len(wheel.get(23)) == 12
    assert len(wheel.get(31)) == 9
    assert len(wheel.get(35)) == 8
    assert len(wheel.all_outcomes) == 129 + 11

    #test_gen_dozen_bets():
    bb.gen_dozen_bets(wheel)
    assert len(wheel.get(3)) == 7
    assert len(wheel.get(9)) == 10
    assert len(wheel.get(23)) == 13
    assert len(wheel.get(31)) == 10
    assert len(wheel.get(35)) == 9
    assert len(wheel.all_outcomes) == 140 + 3

    #test_gen_column_bets():
    bb.gen_column_bets(wheel)
    assert len(wheel.get(3)) == 8
    assert len(wheel.get(9)) == 11
    assert len(wheel.get(23)) == 14
    assert len(wheel.get(31)) == 11
    assert len(wheel.get(35)) == 10
    assert len(wheel.all_outcomes) == 143 + 3


    #test_gen_even_money_bets():
    bb.gen_even_money_bets(wheel)
    assert len(wheel.get(3)) == 11
    assert len(wheel.get(9)) == 14
    assert len(wheel.get(23)) == 17
    assert len(wheel.get(31)) == 14
    assert len(wheel.get(35)) == 13
    assert len(wheel.all_outcomes) == 146 + 6

    
    #test_gen_five_bets():
    bb.gen_five_bets(wheel)
    assert len(wheel.get(0)) == 2
    assert len(wheel.get(37)) == 2
    assert len(wheel.all_outcomes) == 152 + 1
    


def test_buildBins():
    bb.buildBins(wheel)
    assert len(wheel.get(3)) == 11
    assert len(wheel.get(9)) == 14
    assert len(wheel.get(23)) == 17
    assert len(wheel.get(31)) == 14
    assert len(wheel.get(35)) == 13
    assert len(wheel.get(0)) == 2
    assert len(wheel.get(37)) == 2
    assert len(wheel.all_outcomes) == 153

