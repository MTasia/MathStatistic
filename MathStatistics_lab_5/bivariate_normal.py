from math import pi, sqrt, exp
from scipy.stats import multivariate_normal


def b_normal(x_mean: float, y_mean: float, x_div: float, y_div: float, r: float, size: int):
    # return 1 / (2 * pi * x_div * y_div * sqrt(1 - r ** 2)) * exp(
    #     -1 / (2 * (1 - r ** 2)) * (
    #                 ((x - x_mean) ** 2) / x_div ** 2 - 2 * r * (x - x_mean) * (y - y_mean) / (x_div * y_div) + (
    #                     y - y_mean) ** 2 / y_div ** 2))
    cov_matrix = ((x_div ** 2, r * x_div * y_div), (r * x_div * y_div, y_div ** 2))
    mean_vec = (x_mean, y_mean)
    return tuple(zip(*multivariate_normal.rvs(mean=mean_vec, cov=cov_matrix, size=size)))

