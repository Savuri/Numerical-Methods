from math import cos, exp


def f11(x, y):
    return (x - x ** 2) * y


def f21(x, y):
    return 2 * x - 12 - 0.25 * exp(0.25 * x)


def f31(x, y):
    return cos(y[0] + 1.1 * y[1]) + 2.1


def f32(x, y):
    return 1.1 / (x + 2.1 * y[0] ** 2) + x + 1


def f41(x, y):
    return y[1] * 2 - 3 * y[0]


def f42(x, y):
    return y[1] - 2 * y[0]