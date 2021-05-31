from norm_sample_2d import norm_sample_2d
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np


def draw_sample_points(sample: norm_sample_2d, is_separate: bool = True):
    for x, y in zip(*sample.get_data()):
        plt.scatter(x, y)
    if is_separate:
        plt.show()


def draw_ellipse(sample: norm_sample_2d, mixed: bool):
    y_1, y_2 = list(), list()
    x_max = max(abs(min(sample.get_data()[0])), abs(max(sample.get_data()[0])))
    x_min = -x_max
    xs = np.linspace(x_min, x_max, num=10000)

    tmp_values = []
    for x in xs:
        tmp_values.append(
            -((x - sample.get_x_mean()) ** 2 / sample.get_x_div() ** 2 * (sample.get_cor_coef() ** 2 - 1)))
    c = max(tmp_values)

    for x in xs:
        y_1.append(
            sample.get_y_div() * (sample.get_cor_coef() * (x - sample.get_x_mean()) / sample.get_x_div() + sqrt(
                ((x - sample.get_x_mean()) ** 2 / sample.get_x_div() ** 2) * (
                        sample.get_cor_coef() ** 2 - 1) + c)) + sample.get_y_mean())
        y_2.append(
            sample.get_y_div() * (sample.get_cor_coef() * (x - sample.get_x_mean()) / sample.get_x_div() - sqrt(
                ((x - sample.get_x_mean()) ** 2 / sample.get_x_div() ** 2) * (
                        sample.get_cor_coef() ** 2 - 1) + c)) + sample.get_y_mean())
    plt.figure(figsize=(6, 6))

    title = str(len(sample.get_data()[0])) + " elements, correlation coefficient = " + str(sample.get_cor_coef())

    plt.scatter(xs, y_1, c="#686FAB", s=1)
    plt.scatter(xs, y_2, c="#686FAB", s=1)
    plt.grid()

    draw_sample_points(sample, is_separate=False)
    plt.xlim((-3, 3))
    plt.ylim((-3, 3))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.show()
