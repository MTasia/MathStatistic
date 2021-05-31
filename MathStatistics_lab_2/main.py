import sample_getter as get_sample
import prob_utils as num_chars


def count_numerical_char(sample_name: str, sample_size: int):
    s_mean = list()
    med = list()
    extr = list()
    quart = list()
    t_mean = list()
    for i in range(1000):
        sample = get_sample_by_name(sample_name, sample_size)
        s_mean.append(num_chars.count_sample_mean(sample))
        med.append(num_chars.count_sample_median(sample))
        extr.append(num_chars.half_sum_extreme(sample))
        quart.append(num_chars.half_sum_quart(sample))
        t_mean.append(num_chars.truncated_mean(sample))
    return s_mean, med, extr, quart, t_mean


def count_disp_values(numerical_chars: tuple):
    disps = list()
    for numerical_char in numerical_chars:
        tmp_sample = list()
        for elem in numerical_char:
            tmp_sample.append(elem**2)
        disps.append(num_chars.count_sample_mean(tuple(tmp_sample)) - num_chars.count_sample_mean(
            tuple(numerical_char)) ** 2)
    return disps


def count_mean_values(numerical_chars: tuple):
    means = list()
    for elem in numerical_chars:
        means.append(num_chars.count_sample_mean(tuple(elem)))
    return means


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


def run():
    available_distributions = ["normal", "cauchy", "laplace", "poisson", "uniform"]
    sample_sizes = [10, 100, 1000]

    for distr in available_distributions:
        for size in sample_sizes:
            numerical_chars = count_numerical_char(distr, size)
            print(
                distr + ", n = " + str(size) + "\nE(z): " + str(count_mean_values(numerical_chars)) + "\nD(z): " + str(
                    count_disp_values(numerical_chars)))
        print()


run()
