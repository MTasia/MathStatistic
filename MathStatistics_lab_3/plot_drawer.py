import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def set_settings():
    large = 22
    med = 16
    params = {'legend.fontsize': med,
              'figure.figsize': (16, 10),
              'axes.labelsize': med,
              'axes.titlesize': med,
              'xtick.labelsize': med,
              'ytick.labelsize': med,
              'figure.titlesize': large}
    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')
    sns.set_style("white")


def draw_distribution_plot(data, name: str):
    # Первый подграфик
    ax1 = plt.subplot(211)
    plt.title(name, fontsize=20)
    sns.boxplot(data=data[0], orient="h")
    # Второй подграфик
    plt.subplot(212, sharex=ax1)
    sns.boxplot(data=data[1], orient="h")
    plt.show()
