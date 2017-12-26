import pytest
from outcome import Outcome
from bin import Bin
from wheel import Wheel
from non_rnd import Non_rnd

# outcomes
o0 = Outcome('0', 35)
o37 = Outcome('00', 35)
o5 = Outcome('Five Bet', 6)

def test_addOutcomes():
    # wheel
    wheel = Wheel()
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


def test_wheel_spin():
    wheel = Wheel(rng=Non_rnd([0,37]))
    # add outcomes to wheel
    wheel.addOutcome(0,o0)
    wheel.addOutcome(0,o5)
    wheel.addOutcome(37,o37)
    wheel.addOutcome(37,o5)
    b0 = frozenset([o0, o5])
    b37 = frozenset([o37, o5])
    assert wheel.next() == b0
    assert wheel.next() == b37
      
