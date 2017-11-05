import pytest
import random
from ..outcome import Outcome
from ..wheel import Wheel

o0 = Outcome('0', 35)
o37 = Outcome('00', 35)
o5 = Outcome('Five Bet', 6)

def test_wheel():
    wheel = Wheel()
    wheel.addOutcome(0,o0)
    wheel.addOutcome(0,o5)
    wheel.addOutcome(37,o37)
    wheel.addOutcome(37,o5)