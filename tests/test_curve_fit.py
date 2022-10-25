"""
Tests for functions used in scipy's curve fit.
"""

from cracking_the_coding_interview.curve_fit import log_func, exp_func, lin_func


def test_log_func():
    assert log_func(x=0, a=1, b=1, c=1) == 1


def test_exp_func():
    assert exp_func(x=0, a=1, b=1, c=1) == 2


def test_lin_func():
    assert lin_func(x=1, a=1, b=-1) == 0
    assert lin_func(x=1, a=1, b=0) == 1
    assert lin_func(x=-1, a=1, b=0) == -1
