import numpy as np
from math import floor


def get_mean(array: np.array):
    tmp_sum = 0
    for elem in array:
        tmp_sum += elem
    return tmp_sum / len(array)


def get_median(array: np.array):
    if len(array) % 2 == 1:
        return array[int((len(array) - 1) / 2 + 1)]
    return (array[int(len(array) / 2)] + array[int(len(array) / 2 + 1)]) / 2


def lsm(x: np.array, y: np.array):
    x_mean, y_mean = get_mean(x), get_mean(y)
    beta_1 = (get_mean(x * y) - x_mean * y_mean) / (get_mean(x * x) - x_mean ** 2)
    beta_0 = y_mean - x_mean * beta_1
    return beta_0, beta_1


def lad(x: np.array, y: np.array):
    n = len(x)
    tmp_sum = 0
    x_med, y_med = get_median(x), get_median(y)
    for x_i, y_i in zip(x, y):
        tmp_sum += np.sign(x_i - x_med) * np.sign(y_i - y_med)
    r_q = tmp_sum / n
    l = int(floor(n / 4)) + 1 if n % 4 != 0 else int(n / 4)
    j = n - l + 1
    q_y, q_x = (y[j] - y[l]), (x[j] - x[l])

    beta_1 = r_q * q_y / q_x
    beta_0 = y_med - beta_1 * x_med

    return beta_0, beta_1
