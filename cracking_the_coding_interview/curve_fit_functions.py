"""
Functions for use in scipy's curve fit.
"""

import numpy as np


def log_func(x, a, b, c):
    return a * np.log(b + x) + c


def exp_func(x, a, b, c):
    return a * np.exp(-b * x) + c


def lin_func(x, a, b):
    return (a * x) + b
