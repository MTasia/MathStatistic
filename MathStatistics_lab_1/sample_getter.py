from scipy.stats import norm, poisson, cauchy, laplace, uniform
from math import sqrt


def norm_distribution(sample_size: int, loc=0, scale=1):
    sample = norm(loc, scale).rvs(size=sample_size)
    sample.sort()
    return tuple(sample)


def poisson_distribution(sample_size: int, mu=10):
    sample = poisson(mu).rvs(size=sample_size)
    sample.sort()
    return tuple(sample)


def cauchy_distribution(sample_size: int, loc=0, scale=1):
    sample = cauchy(loc, scale).rvs(size=sample_size)
    sample.sort()
    return tuple(sample)


def laplace_distribution(sample_size: int, loc=0, scale=1/sqrt(2)):
    sample = laplace(loc, scale).rvs(size=sample_size)
    sample.sort()
    return tuple(sample)


def uniform_distribution(sample_size: int, loc=-sqrt(3), scale=sqrt(3)):
    sample = uniform(loc, scale).rvs(size=sample_size)
    sample.sort()
    return tuple(sample)
