import pytest
from ..outcome import Outcome
from ..bet import Bet
from ..binBuilder import BinBuilder
from ..wheel import create_wheel

wheel = create_wheel()

split47 = Bet(100, wheel.getOutcome('4,7'))
line7 = Bet(100, wheel.getOutcome('7,8,9'))
low = Bet(100, wheel.getOutcome('Low'))
dzero = Bet(100, wheel.getOutcome('00'))

def test_wheel_get():
    print(wheel.getOutcome('Low'))
    print(wheel.getOutcome('00'))
    # change to 0 to see the print statements
    assert 1
    
def test_print_bets():
    print(split47)
    print(line7)
    print(low)
    print(dzero)
    # change to 0 to see the print statements
    assert 1

def test_winAmount():
    assert split47.winAmount() == 1800
    assert line7.winAmount() == 1200
    assert low.winAmount() == 200
    assert dzero.winAmount() == 3600

def test_loseAmount():
    assert split47.loseAmount() == 100
    assert line7.loseAmount() == 100
    assert low.loseAmount() == 100
    assert dzero.loseAmount() == 100





    


