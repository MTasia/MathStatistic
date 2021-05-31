from math import inf
import numpy as np


def get_mean(array: np.array):
    tmp_sum = 0
    for elem in array:
        tmp_sum += elem
    return tmp_sum / len(array)


def mle(sample: np.array):
    mu = get_mean(sample)
    tmp_sum = 0
    for x in sample:
        tmp_sum += (x - mu) ** 2
    sigma = tmp_sum / len(sample)
    return mu, sigma


def chi_square(sample: np.array, k: int, func, chi_max: float, mu: float = 0, sigma: float = 1):
    b_l, b_r = -1, 1
    borders = np.empty(k + 1)
    borders[0], borders[-1] = -inf, inf
    for i, value in zip(range(1, k), np.linspace(b_l, b_r, num=k - 1)):
        borders[i] = value
    xi_sq = 0
    probabilities = np.zeros(k)
    frequencies = np.zeros(k)
    print("i & границы $\\Delta_i$ & $n_i$ & $p_i$ & $np_i$ & $n_i-np_i$ & $\\frac{(n_i-np_i)^2}{np_i}$ \\\\ \\hline")
    for i in range(1, k + 1):
        probabilities[i - 1] = func.cdf(borders[i], loc=mu, scale=sigma) - func.cdf(borders[i - 1], loc=mu, scale=sigma)
        for x in sample:
            if borders[i - 1] < x <= borders[i]:
                frequencies[i - 1] += 1
        tmp_chi = (frequencies[i - 1] - len(sample) * probabilities[i - 1]) ** 2 / (len(sample) * probabilities[i - 1])
        print(i, "& [", round(borders[i - 1], 3),",",round(borders[i], 3), "] &", round(frequencies[i - 1], 3), "&",
              round(probabilities[i - 1], 3), "&", round(len(sample) * probabilities[i - 1], 3), "&",
              round(frequencies[i - 1] - len(sample) * probabilities[i - 1], 3), "&", round(tmp_chi, 3),
              "\\\\ \\hline")
        xi_sq += tmp_chi
    return xi_sq, xi_sq < chi_max
