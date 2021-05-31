import sample_getter as get_sample
import plot_drawer as pltd
from prob_utils import count_sample_median, count_sample_mean
import pandas as pd
from scipy.stats import norm

theoretical_proportions = {
    "normal": 0.007,
    "cauchy": 0.156,
    "laplace": 0.063,
    "poisson": 0.008,
    "uniform": 0
}

def get_sample_by_name(entered: str, size: int):
    # generate and draw samples of 10 elements
    if entered == "normal":
        return get_sample.norm_distribution(size)
    elif entered == "cauchy":
        return get_sample.cauchy_distribution(size)
    elif entered == "laplace":
        return get_sample.laplace_distribution(size)
    elif entered == "poisson":
        return get_sample.poisson_distribution(size)
    elif entered == "uniform":
        return get_sample.uniform_distribution(size)
    else:
        return False


def count_empirical_outburst(sample: tuple):
    if len(sample) % 2 == 1:
        first_quart = count_sample_median(sample[0:(len(sample) - 1) / 2 + 1])
        third_quart = count_sample_median(sample[(len(sample) - 1) / 2: -1])
    else:
        first_quart = count_sample_median(sample[0:int(len(sample) / 2)])
        third_quart = count_sample_median(sample[int(len(sample) / 2): -1])
    count = 0
    for elem in sample:
        if elem < first_quart - 1.5 * (third_quart - first_quart) or elem > third_quart + 1.5 * (
                third_quart - first_quart):
            count += 1
    return count / len(sample)


def run():
    __available = ["normal", "cauchy", "laplace", "poisson", "uniform"]

    print("Available distributions:")
    for unit in __available:
        print("\t" + unit + ";")
    print("If you want to shut program down, type \"exit\"")

    while True:
        entered = input("\nEnter desired distribution name: ")

        if entered == "exit":
            break
        elif entered not in __available:
            print("wrong distribution name")
            continue

        outburst_20 = list()
        outburst_100 = list()

        for i in range(1000):
            sample_20 = get_sample_by_name(entered, 20)
            sample_100 = get_sample_by_name(entered, 100)
            outburst_20.append(count_empirical_outburst(sample_20))
            outburst_100.append(count_empirical_outburst(sample_100))
        df_20 = pd.DataFrame({"20": sample_20})
        df_100 = pd.DataFrame({"100": sample_100})
        print("Empirical outburst proportion for sample[20]: " + str(count_sample_mean(outburst_20)))
        print("Empirical outburst proportion for sample[100]: " + str(count_sample_mean(outburst_100)))
        print("Theoretical outburst proportion this distribution: " + str(theoretical_proportions.get(entered)))
        pltd.draw_distribution_plot([df_20, df_100], entered)


run()
