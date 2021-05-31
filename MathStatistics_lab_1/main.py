import plot_drawer
import sample_getter as get_sample
import seaborn as sns


def print_plot_by_name(entered: str):
    # generate and draw samples of 10 elements
    __sizes = (10, 50, 1000)
    for size in __sizes:
        if entered == "normal":
            normal = get_sample.norm_distribution(size)
            plot_drawer.draw_distribution_hist(normal, entered)
        elif entered == "cauchy":
            cauchy = get_sample.cauchy_distribution(size)
            plot_drawer.draw_distribution_hist(cauchy, entered)
        elif entered == "laplace":
            laplace = get_sample.laplace_distribution(size)
            plot_drawer.draw_distribution_hist(laplace, entered)
        elif entered == "poisson":
            poisson10 = get_sample.poisson_distribution(size)
            plot_drawer.draw_distribution_hist(poisson10, entered)
        elif entered == "uniform":
            uniform = get_sample.uniform_distribution(size)
            plot_drawer.draw_distribution_hist(uniform, entered)


if __name__ == '__main__':
    __available = ["normal", "cauchy", "laplace", "poisson", "uniform"]

    print("Available distributions:")
    for unit in __available:
        print("\t" + unit + ";")
    print("If you want to shut program down, type \"exit\"")

    while True:
        entered = input("Enter desired distribution name: ")

        if entered == "exit":
            break
        elif entered not in __available:
            print("wrong distribution name")
            continue

        print_plot_by_name(entered)


