import pytest
import random
from ..outcome import Outcome
from ..wheel import Wheel

# outcomes
o0 = Outcome('0', 35)
o37 = Outcome('00', 35)
o5 = Outcome('Five Bet', 6)
# wheel
wheel = Wheel()

def test_addOutcomes():
    # add outcomes to wheel
    wheel.addOutcome(0,o0)
    wheel.addOutcome(0,o5)
    wheel.addOutcome(37,o37)
    wheel.addOutcome(37,o5)
    assert o0 in wheel.bins[0]
    assert o5 in wheel.bins[0]
    assert o37 in wheel.bins[37]
    assert len(wheel.bins[0]) == 2
    assert len(wheel.bins[37]) == 2


    