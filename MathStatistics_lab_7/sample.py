from scipy.stats import norm


def get_sample(size: int = 100):
    return norm.rvs(size=size)
