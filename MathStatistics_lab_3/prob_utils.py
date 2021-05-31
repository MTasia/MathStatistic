# Расчёт выборочной медианы
def count_sample_median(sample: tuple):
    assert len(sample) > 0
    if len(sample) % 2 == 1:
        return sample[int((len(sample) - 1) / 2 + 1)]
    return (sample[int(len(sample) / 2)] + sample[int(len(sample) / 2 + 1)]) / 2


# Расчёт выборочного среднего
def count_sample_mean(sample: tuple):
    _sum = 0
    for elem in sample:
        _sum += elem
    return _sum / len(sample)
