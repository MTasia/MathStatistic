# Расчёт выборочного среднего
def count_sample_mean(sample: tuple):
    _sum = 0
    for elem in sample:
        _sum += elem
    return _sum / len(sample)


# Расчёт выборочной медианы
def count_sample_median(sample: tuple):
    assert len(sample) > 0
    if len(sample) % 2 == 1:
        return sample[int((len(sample) - 1) / 2 + 1)]
    return (sample[int(len(sample) / 2)] + sample[int(len(sample) / 2 + 1)]) / 2


# Расчёт полусуммы экстремальны выборочных элементов
def half_sum_extreme(sample: tuple):
    assert len(sample) > 0
    return (sample[0] + sample[-1]) / 2


# Расчёт полусуммы кваритлей
def half_sum_quart(sample: tuple):
    if len(sample) % 2 == 1:
        first_quart = count_sample_median(sample[0:(len(sample) - 1) / 2 + 1])
        third_quart = count_sample_median(sample[(len(sample) - 1) / 2: -1])
    else:
        first_quart = count_sample_median(sample[0:int(len(sample) / 2)])
        third_quart = count_sample_median(sample[int(len(sample) / 2): -1])
    return (first_quart + third_quart) / 2


# Расчёт усеченного среднего
def truncated_mean(sample: tuple):
    r = int(len(sample) / 4)
    _sum = 0
    for i in range(r + 1, len(sample) - r):
        _sum += sample[i]
    return _sum / (len(sample) - 2 * r)
