import pytest
from outcome import Outcome

o1 = Outcome("Red", 1)
o2 = Outcome("Red", 2)
o3 = Outcome("18", 35)


def test_outcome_eq():
    assert o1 == o2


def test_outcome_ne():
    assert o1 != o3


def test_hash():
    assert hash(o1) == hash(o2)


def test_winAmount():
    assert o3.winAmount(20) == 700
