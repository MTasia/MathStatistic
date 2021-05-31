import matplotlib.pyplot as plt
from scipy.stats import norm, poisson, cauchy, laplace, uniform
from math import sqrt

def draw_distribution_hist(data: list, name: str):
    plt.grid(b=True)
    plt.hist(data, density=True, histtype="bar", stacked=True, edgecolor="black", bins=20)
    draw_distribution_plot(data, name)
    plt.xlabel("Values")
    plt.ylabel("Density")
    plt.title(name + " distribution, " + str(len(data)) + " elements")
    plt.show()


def draw_distribution_plot(data: list, name: str):
    plot_y = list()
    extended_data = list(data)
    extended_data.append(data[0]-0.05)
    extended_data.append(data[-1] + 0.05)
    extended_data.sort()
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
            plot_y.append(uniform.pdf(i, -sqrt(3), sqrt(3)))
    elif name == "laplace":
        for i in extended_data:
            plot_y.append(laplace.pdf(i, 0, 1/sqrt(2)))
    plt.plot(extended_data, plot_y, lw=4, color="black")
    plt.plot(extended_data, plot_y, lw=3, color="red")
