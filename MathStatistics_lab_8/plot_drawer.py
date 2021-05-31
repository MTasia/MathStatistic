import numpy as np
import matplotlib.pyplot as plt
from math import log10
from utils import get_fisher_criteria


def draw_signal_plot(sample: np.array, intervals: tuple):
    for interval in intervals:
        sample_slice = sample[interval[0]:interval[-1]]
        group_count = int(3.3 * log10(len(sample_slice)))

        if intervals.index(interval) == 0 or intervals.index(interval) == 4:
            color = "red"
        elif intervals.index(interval) == 1 or intervals.index(interval) == 3:
            color = "green"
        else:
            color = "blue"

        print("fisher criteria", get_fisher_criteria(sample_slice, group_count), group_count, "intervals")
        plt.plot([i for i in range(interval[0], interval[1])], sample_slice, linewidth=2, c=color)
    plt.title("Signal plot")
    plt.grid()
    plt.legend(("Background", "Transition", "Signal"))
    plt.show()


def draw_signal_hist(sample: np.array, bins: int=50):
    plt.hist(sample, density=True, bins=bins)
    plt.title("Signal histogram")
    plt.grid()
    plt.show()
