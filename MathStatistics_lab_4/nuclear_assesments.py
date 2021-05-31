from math import sqrt, exp, pi
import matplotlib.pyplot as plt
import sample_getter as sg
import plot_drawer as pd


# Расчёт выборочного среднего
def count_sample_mean(sample: tuple):
    _sum = 0.0
    for elem in sample:
        _sum += elem
    return float(_sum / len(sample))


def count_sample_deviation(sample: tuple):
    _sum = 0
    mean = count_sample_mean(sample)
    for elem in sample:
        _sum += (elem - mean) ** 2
    return sqrt(_sum / (len(sample) - 1))


# Гауссово ядро
def kernel_func(x: float):
    return exp(-x * x / 2) / sqrt(2 * pi)


# Ядерная оценка
def nuclear_assessment(x: float, sample: tuple, h_coef: float):
    sigma = count_sample_deviation(sample)
    h = 1.06 * sigma * (len(sample) ** (-0.2))
    kernel_sum = 0
    for elem in sample:
        kernel_sum += kernel_func((x - elem) / (h * h_coef))
    return 1 / (len(sample) * h * h_coef) * kernel_sum


# Ядерная оценка плотности распределения
def build_nuclear_assessment_plot(sample: tuple, entered: str, size: int, step=0.01):
    scale = int(1 / step)
    if entered != "poisson":
        borders = [-4, 4] if not entered == "poisson" else [6, 14]
        sample_range = [x / float(scale) for x in range(borders[0] * scale, borders[1] * scale, int(step * scale))]
    else:
        borders = [6, 15]
        sample_range = [x for x in range(borders[0], borders[1])]
        nuclear_range = [x / float(scale) for x in range(borders[0] * scale, borders[1] * scale, int(step * scale))]
    figure, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, sharey=True)
    pd.set_nuclear_settings((ax1, ax2, ax3))
    for h_coef, ax in zip([0.5, 1, 2], (ax1, ax2, ax3)):
        sample_values = list()
        if entered != "poisson":
            for x in sample_range:
                sample_values.append(nuclear_assessment(x, sample, h_coef))
            ax.plot(sample_range, sample_values, label="Nuclear assessment")
        else:
            for x in nuclear_range:
                sample_values.append(nuclear_assessment(x, sample, h_coef))
            ax.plot(nuclear_range, sample_values, label="Nuclear assessment")
        pd.draw_distribution_density_plot(sample_range, entered, ax)
        # ax.plot(sample_range, sample_values, label="Nuclear assessment")

    z

# Построение эмпирической функции
