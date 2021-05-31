from function import func
import numpy as np
import matplotlib.pyplot as plt
from criteria import lsm, lad


def main(altered: bool = False):
    x = np.linspace(-1.8, 2, 20)
    y = func(2, 2, x)

    if altered:
        y[0] += 10
        y[-1] -= 10

    a_lsm, b_lsm = lsm(x, y)
    print("МНК: a =", a_lsm, ", b =", b_lsm)
    a_lad, b_lad = lad(sorted(x), sorted(y))
    print("МНМ: a =", a_lad, ", b =", b_lad)

    y_lsm = func(a_lsm, b_lsm, x, with_errors=False)
    y_lad = func(a_lad, b_lad, x, with_errors=False)
    y_def = func(2, 2, x, with_errors=False)

    plt.scatter(x, y)
    plt.plot(x, y_lad, c="blue")
    plt.plot(x, y_lsm, c="red")
    plt.plot(x, y_def, c="green")

    plt.legend(("Метод наименьших модулей", "Метод наименьших квадратов", "Эталонная модель", "Элементы выборки"))
    plt.grid()

    title = "Выборка с возмущениями" if altered else "Выборка без возмущений"
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("Y")
    plt.show()


main(altered=False)
