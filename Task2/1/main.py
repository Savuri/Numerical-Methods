from calc import runge
from functions import *
import numpy as np
import matplotlib.pyplot as plt


def print_dots(x, y, n):
    for i in range(x.size):
        tmp = ""
        for j in range(n):
            tmp += ", "
            tmp += '{:3.7f}'.format(y[j][i])
        print("(" + '{:3.7f}'.format(x[i]) + tmp + ")", end=" ")
    print()


if __name__ == '__main__':
    step = float(input("Input step size: "))

    if step <= 0:
        raise Exception("Incorrect data")

    n = int(input("Input steps count: "))

    if n < 0:
        raise Exception("Incorrect data")

    test_number = int(input("Input test number 1 (Table1-6), 2 (additional test 1), "
                            "3 (Table 2-5),  4(additional test 2): "))

    if test_number < 1 and test_number > 4:
        raise Exception("Incorrect data")

    runge_i = int(input("Input order of accuracy: 2 for Runge-Kutta(O(2)), 4 for Runge-Kutta(O(4)): "))

    if runge_i != 2 and runge_i != 4:
        raise Exception("Incorrect data")

    functions = []

    if test_number == 1:
        x0 = 0
        y0 = np.array([1])
        functions.append(f11)
    elif test_number == 2:
        x0 = 0
        y0 = np.array([0])
        functions.append(f21)
    elif test_number == 3:
        x0 = 0
        y0 = np.array([1, 0.05])
        functions.append(f31)
        functions.append(f32)
    elif test_number == 4:
        x0 = 0
        y0 = np.array([1, 2])
        functions.append(f41)
        functions.append(f42)
    else:
        raise Exception("Incorrect data")

    x, y = runge(functions, x0, y0, step, n, runge_i)

    print_dots(x, y, y.size // (n + 1))

    if test_number == 1 or test_number == 2:
        plt.plot(x, y[0])
        plt.show()
    elif test_number == 3 or test_number == 4:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x, y[0], y[1], label='solution')
        ax.set_xlabel('x Label')
        ax.set_ylabel('y1 Label')
        ax.set_zlabel('y2 Label')
        ax.legend()
        plt.show()
