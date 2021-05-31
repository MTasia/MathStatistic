from math import sqrt
from scipy.stats import norm, cauchy, laplace, poisson, uniform, rv_continuous, rv_discrete
import matplotlib.pyplot as plt


def draw_distribution_cumulative_plot(data: list, name: str, ax: plt.axes):
    plot_y = list()
    extended_data = list(data)
    extended_data.append(data[0] - 0.05)
    extended_data.append(data[-1] + 0.05)
    extended_data.sort()
    if name == "normal":
        for i in extended_data:
            plot_y.append(norm.cdf(i))
    elif name == "cauchy":
        for i in extended_data:
            plot_y.append(cauchy.cdf(i))
    elif name == "poisson":
        for i in extended_data:
            plot_y.append(poisson.cdf(i, 10))
    elif name == "uniform":
        for i in extended_data:
            plot_y.append(uniform.cdf(i, -sqrt(3), sqrt(3) * 2))
    elif name == "laplace":
        for i in extended_data:
            plot_y.append(laplace.cdf(i, 0, 1 / sqrt(2)))
    ax.plot(extended_data, plot_y, color="red", label="Actual cumulative function")


def draw_distribution_density_plot(data: list, name: str, ax: plt.axes):
    plot_y = list()
    extended_data = list(data)
    if name == "normal":
        for i in extended_data:
            plot_y.append(norm.pdf(i))
    elif name == "cauchy":
        for i in extended_data:
            plot_y.append(cauchy.pdf(i))
    elif name == "poisson":
        for i in extended_data:
            plot_y.append(poisson.pmf(i, 10))
    elif name == "uniform":
        for i in extended_data:
            plot_y.append(uniform.pdf(i, -sqrt(3), sqrt(3) * 2))
    elif name == "laplace":
        for i in extended_data:
            plot_y.append(laplace.pdf(i, 0, 1 / sqrt(2)))
    ax.plot(extended_data, plot_y, color="red", label="Density function")


def set_nuclear_settings(axes: tuple):
    for ax, coef in zip(axes, (0.5, 1, 2)):
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("h * " + str(coef))


def draw_empirical_func_plot(sample: list, entered: str, step=0.01):
    fig, ax = plt.subplots()
    ax.hist(sample, histtype='step', cumulative=True, bins=len(sample), density=True,
            label="Empirical cumulative function")
    draw_distribution_cumulative_plot(sample, entered, ax)
    plt.title("Empirical cumulative function plot for " + entered + "distribution, " + str(len(sample)) + " elements")
    plt.legend()
    plt.show()
