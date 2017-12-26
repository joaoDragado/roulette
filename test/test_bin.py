import pytest
from outcome import Outcome
from bin import Bin

o1 = Outcome('0', 35)
o2 = Outcome('00', 35)
o4 = Outcome('1', 35)
o5 = Outcome('Red', 1)
o6 = Outcome('Odd', 1)
o8 = Outcome('Column 1', 2)
o10 = Outcome('Split 1-2', 17)
o11 = Outcome('Split 1-4', 17)
o12 = Outcome('Street 1-2-3', 11)
o13 = Outcome('Corner 1-2-4-5', 8)
o14 = Outcome('Five Bet', 6)
o15 = Outcome('Line 1-2-3-4-5-6', 5)
o17 = Outcome('Dozen 1', 2)
o18 = Outcome('Low', 1)


def test_bins():
    b1 = Bin([o1,o14])
    b2 = Bin([o2,o14])
    b3 = Bin([o4,o5,o6,o8,o10,o11,o12,o13,o14,o15,o17,o18])
    # check class Bin extends frozenset
    assert issubclass(Bin, frozenset)
    # check Bin instances subclass frozenset
    assert isinstance(b1,frozenset)
    assert isinstance(b2,frozenset)
    assert isinstance(b3,frozenset)

