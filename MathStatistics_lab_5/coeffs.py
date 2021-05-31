from norm_sample_2d import norm_sample_2d
from math import sqrt
import numpy as np


def pearson(sample: list):
    upper_sum = 0
    lower_sum_a = 0
    lower_sum_b = 0
    x_mean = np.mean(sample[0])
    y_mean = np.mean(sample[1])
    for x, y in zip(*sample):
        upper_sum += (x - x_mean) * (y - y_mean)
        lower_sum_a += (x - x_mean) ** 2
        lower_sum_b += (y - y_mean) ** 2
    lower_sum = sqrt(lower_sum_a * lower_sum_b)
    return upper_sum / lower_sum


def spearman(sample: list):
    orig_x = dict()
    orig_y = dict()

    sorted_xs = sorted(sample[0])
    sorted_ys = sorted(sample[1])

    for x in sample[0]:
        for sx in sorted_xs:
            if x == sx:
                orig_x.update({x: sorted_xs.index(sx) + 1})

    for y in sample[1]:
        for sy in sorted_ys:
            if y == sy:
                orig_y.update({y: sorted_ys.index(sy) + 1})

    upper_sum = 0
    lower_sum_a = 0
    lower_sum_b = 0
    sample_len = len(sample[0])

    for x, y in zip(orig_x.values(), orig_y.values()):
        upper_sum += (x - (sample_len + 1) / 2) * (y - (sample_len + 1) / 2)
        lower_sum_a += (x - (sample_len + 1) / 2) ** 2
        lower_sum_b += (y - (sample_len + 1) / 2) ** 2
    lower_sum = sqrt(lower_sum_a * lower_sum_b)
    return upper_sum / lower_sum


def quadrant(sample: list):
    q1, q2, q3, q4 = 0, 0, 0, 0
    x_mean = np.mean(sample[0])
    y_mean = np.mean(sample[1])
    for x, y in zip(*sample):
        if x < x_mean:
            if y < y_mean:
                q3 += 1
            else:
                q2 += 1
        else:
            if y < y_mean:
                q4 += 1
            else:
                q1 += 1
    return ((q1 + q3) - (q2 + q4)) / len(sample[0])
