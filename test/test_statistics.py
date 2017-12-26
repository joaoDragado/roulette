import pytest
from statistics import IntegerStatistics

sample =  [10, 8, 13, 9, 11, 14, 6 , 4, 12, 7 , 5]

''' Descriptive statistics for the sample test list
sum 99
count 11
mean 9.0
sum (x-m)**2 110.0
stdev 3.317
'''

stat_list = IntegerStatistics(sample)


def test_IS_list():
    assert len(stat_list) == 11
    assert sum(stat_list) == 99
    assert stat_list.mean() == 9.0
    assert round(stat_list.stdev(), 3) == 3.317
