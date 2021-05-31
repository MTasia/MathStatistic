from scipy.stats import norm
import numpy as np


def func(a: float, b: float, x: np.array, with_errors: bool = True) -> np.array:
    y = np.empty(len(x))
    for i, x_i in enumerate(x):
        err = norm.rvs() if with_errors else 0
        y[i] = a + b * x_i + err
    return y
