import numpy as np
import matplotlib.pyplot as plt
from functions import *

def print_dots(x, y):
    for i in range(x.size):
        print("({:3.7f}, {:3.7f})".format(x[i], y[i]), end="")

        if i != x.size - 1:
            print(", ", end="")
        else:
            print()


if __name__ == '__main__':
    iterations_count = int(input("Input count of iterations: "))
    test_number = int(input("Test number: "))

    if iterations_count < 0:
        raise Exception("Incorrect data")

    if test_number < 1 or test_number > 4:
        raise Exception("Incorrect data")

    if test_number == 1:
        # y'' + 2 * y' - y / x = 3
        # y(0.2)=2
        # 0.5 * y(0.5) - y'(0.5) = 1
        p = p1; q = q1; f = f1

        xa = 0.2; a1 = 1; a2 = 0; a3 = 2
        xb = 0.5; b1 = 1; b2 = 0; b3 = 1
    elif test_number == 2:
        # y'' + y' = 1
        # y'(0) = 0
        # y(1) = 1
        p = p2; q = q2; f = f2

        xa = 0; a1 = 0; a2 = 1; a3 = 0
        xb = 1; b1 = 1; b2 = 0; b3 = 1
    elif test_number == 3:
        # y'' + 2 * y'=1
        # y(0) = 0
        # y'(1) = 1
        p = p3; q = q3; f = f3

        xa = 0; a1 = 1; a2 = 0; a3 = 0
        xb = 1; b1 = 0; b2 = 1; b3 = 1
    else:
        # y'' + 2 * y' - x * y = x^2
        # y'(0.6) = 0.7
        # y(0.9) - 0.5 * y'(0.9) = 1
        f = f4; p = p4; q = q4

        xa = 0.6; a1 = 0; a2 = 1; a3 = 0.7
        xb = 0.9; b1 = 1; b2 = -0.5; b3 = 1

    h = (xb - xa) / iterations_count
    y = np.empty(iterations_count + 1)
    alpha = np.empty(iterations_count)
    betta = np.empty(iterations_count)

    B0 = h * a1 - a2
    C0 = a2
    D0 = h * a3
    alpha[0] = -C0 / B0
    betta[0] = D0 / B0
    x = np.empty(iterations_count + 1)

    for i in range(iterations_count + 1):
        x[i] = xa + i * h

    for i in range(1, iterations_count):
        Ai = 2 - h * p(x[i])
        Bi = -4 + 2 * h ** 2 * q(x[i])
        Ci = 2 + h * p(x[i])
        Di = 2 * h ** 2 * f(x[i])

        alpha[i] = -Ci / (Bi + Ai * alpha[i - 1])
        betta[i] = (Di - Ai * betta[i - 1]) / (Bi + Ai * alpha[i - 1])

    An = -b2
    Bn = h * b1 + b2
    Dn = h * b3
    y[iterations_count] = (Dn - An * betta[iterations_count - 1]) / (An * alpha[iterations_count - 1] + Bn)

    for i in range(iterations_count, 0, -1):
        y[i - 1] = alpha[i - 1] * y[i] + betta[i - 1]

    print_dots(x, y)
    plt.plot(x, y)
    plt.show()
