import pytest
from ..table import Table
from ..bet import Bet
from ..wheel import Wheel

wheel = Wheel()
low = Bet(100, wheel.getOutcome('Low'))
dzero = Bet(100, wheel.getOutcome('00'))
bets = [low, dzero]
tbl = Table()


def test_iter():
    tbl.placeBet(low)
    tbl.placeBet(dzero)
    for i, b in enumerate(tbl):
        assert bets[i] == b
    