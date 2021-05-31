from utils import *
from plot_drawer import draw_signal_plot, draw_signal_hist

size = 1024
signal_index = 8


def main():
    sample = get_sample(signal_index, size=size)
    intervals = ((0, 220), (220, 320), (320, 725), (725, 820), (820, 1024))
    draw_signal_plot(sample, intervals)
    draw_signal_hist(sample)


def filtered_sample(sample: np.array):
    filtered = list()
    for i in range(0, len(sample)):
        if i - 1 > 0 and i + 1 < len(sample):
            filtered.append((sample[i - 1] + sample[i + 1]) / 2)
        else:
            filtered.append(sample[i])
    return np.array(filtered)


main()
