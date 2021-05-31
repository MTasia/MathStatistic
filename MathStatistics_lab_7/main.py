from utils import mle, chi_square
from math import log10
import scipy.stats as st

alpha = 0.05
size = 100
k = int(1 + 3.3 * log10(size))  # k = 7
step = 0.2
b_l, b_r = -1, 1
chi_max = 12.59


def main():
    normal_sample = st.norm.rvs(size=size)
    mu, sigma = mle(normal_sample)

    print("Normal estimation:", chi_square(normal_sample, k, st.norm, chi_max, mu=mu, sigma=sigma), mu, sigma)

    laplace_sample = st.laplace.rvs(size=20)
    mu, sigma = mle(laplace_sample)
    print("Laplace estimation:", chi_square(laplace_sample, 5, st.norm, 9.49), mu, sigma)

    uniform_sample = st.uniform.rvs(loc=-1.5, scale=3, size=20)
    mu, sigma = mle(uniform_sample)
    print("Uniform estimation:", chi_square(uniform_sample, 5, st.norm, 9.49), mu, sigma)


main()
