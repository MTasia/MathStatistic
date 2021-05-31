from scipy.stats import norm, poisson, cauchy, laplace, uniform
from math import sqrt


def get_sample_by_name(entered: str, size: int):
    # generate and draw samples of 10 elements
    if entered == "normal":
        return norm_distribution(size)
    elif entered == "cauchy":
        return cauchy_distribution(size)
    elif entered == "laplace":
        return laplace_distribution(size)
    elif entered == "poisson":
        return poisson_distribution(size)
    elif entered == "uniform":
        return uniform_distribution(size)
    else:
        return False


def norm_distribution(sample_size: int, loc=0, scale=1):
    sample = norm(loc, scale).rvs(size=sample_size)
    sample.sort()
    return list(sample)


def poisson_distribution(sample_size: int, mu=10):
    sample = poisson(mu).rvs(size=sample_size)
    sample.sort()
    return list(sample)


def cauchy_distribution(sample_size: int, loc=0, scale=1):
    sample = cauchy(loc, scale).rvs(size=sample_size)
    sample.sort()
    return list(sample)


def laplace_distribution(sample_size: int, loc=0, scale=1/sqrt(2)):
    sample = laplace(loc, scale).rvs(size=sample_size)
    sample.sort()
    return list(sample)


def uniform_distribution(sample_size: int, loc=-sqrt(3), scale=sqrt(3) * 2):
    sample = uniform(loc, scale).rvs(size=sample_size)
    sample.sort()
    return list(sample)
