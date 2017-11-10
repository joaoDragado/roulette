import pytest
from ..outcome import Outcome
from ..bet import Bet
from ..binBuilder import BinBuilder
from ..wheel import Wheel

wheel = Wheel()

split47 = Bet(100, wheel.getOutcome('4,7'))
line7 = Bet(100, wheel.getOutcome('7,8,9'))
low = Bet(100, wheel.getOutcome('Low'))
dzero = Bet(100, wheel.getOutcome('00'))

def test_wheel_get():
    print(wheel.getOutcome('Low'))
    print(wheel.getOutcome('00'))
    assert 0
    
def test_print_bets():
    print(split47)
    print(line7)
    print(low)
    print(dzero)
    assert 0







    


