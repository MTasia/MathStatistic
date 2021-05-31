import sample_getter as sg
import matplotlib.pyplot as plt
import scipy.stats as ss
import nuclear_assesments as na
import plot_drawer as pd


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

        for size in [20, 60, 100]:
            sample = sg.get_sample_by_name(entered, size)
            # na.build_nuclear_assessment_plot(sample, entered, size)
            pd.draw_empirical_func_plot(sample, entered)

run()
