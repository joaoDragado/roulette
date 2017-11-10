import pytest
from ..outcome import Outcome
from ..bet import Bet
from ..binBuilder import BinBuilder
from ..wheel import Wheel


def test_wheel():
    wheel = Wheel()
    assert len(wheel.all_outcomes) == 153


