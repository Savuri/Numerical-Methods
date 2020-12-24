import numpy as np


def runge(f, x0, y0, h, steps_count, mode):
    if mode != 2 and mode != 4:
        raise Exception("Incorrect date")

    equations_count = y0.size
    iterations_count = steps_count + 1

    x = np.empty(iterations_count)
    y = np.empty((equations_count, iterations_count))

    for i in range(equations_count):
        y[i][0] = y0[i]

    for i in range(iterations_count):
        x[i] = x0 + i * h

    for i in range(1, iterations_count):
        for j in range(equations_count):
            if mode == 2:
                tmp = f[j](x[i - 1], y[:, i - 1])
                y[j][i] = y[j][i - 1] + h / 2 * (tmp + f[j](x[i - 1] + h, y[:, i - 1] + h * tmp))
            else:
                k1 = f[j](x[i - 1], y[:, i - 1])
                k2 = f[j](x[i - 1] + h / 2, y[:, i - 1] + h / 2 * k1)
                k3 = f[j](x[i - 1] + h / 2, y[:, i - 1] + h / 2 * k2)
                k4 = f[j](x[i - 1] + h / 2, y[:, i - 1] + h * k3)
                y[j][i] = y[j][i - 1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return x, y