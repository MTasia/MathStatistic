import numpy as np


def get_mean(sample: np.array):
    return sum(sample) / len(sample)


def get_sample(index: int, size: int = 1024):
    return np.loadtxt("wave_ampl.txt", usecols=[index * size + i for i in range(1, size + 1)], delimiter=", ")


def get_intra_group_dispersion(sample: np.array, group_count: int):
    dispersions = np.zeros(group_count)
    for i in range(group_count):
        for j in range(int(len(sample) / group_count)):
            dispersions[i] += (sample[i * group_count + j] - get_mean(
                sample[i * group_count:int(i * group_count + len(sample) / group_count)])) ** 2 / (group_count - 1)
    print(get_mean(dispersions))
    return get_mean(dispersions)


def get_inter_group_dispersion(sample: np.array, group_count: int):
    group_means = np.zeros(group_count)
    for i in range(group_count):
        group_means[i] += get_mean(sample[i * group_count:int(i * group_count + len(sample) / group_count)])
    general_mean = get_mean(group_means)
    dispersion = 0
    for i in range(group_count):
        dispersion += (group_means[i] - general_mean) ** 2
    print(group_count * dispersion / (group_count - 1))
    return group_count * dispersion / (group_count - 1)


def get_fisher_criteria(sample: np.array, group_count: int):
    return get_inter_group_dispersion(sample, group_count) / get_intra_group_dispersion(sample, group_count)
