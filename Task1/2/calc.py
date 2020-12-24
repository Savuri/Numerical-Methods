import numpy as np

MAX_ITERATION = 100000


def get_next_1(B, c, x):
    return np.dot(B, x) + c


def get_next(A, F, w, prev):
    next = np.empty((prev.size))

    for i in range(prev.size):
        sum1 = 0.0

        for j in range(i):
            sum1 += A[i][j] / A[i][i] * next[j]

        sum2 = 0.0
        for j in range(i, prev.size):
            sum2 += A[i][j] / A[i][i] * prev[j]
        next[i] = prev[i] + w * (F[i] / A[i][i] - sum1 - sum2)
    return next


def criteria(B):
    tmp1, _ = np.linalg.eig(B)
    tmp1 = tmp1.astype(complex)
    tmp1 = np.abs(tmp1)
    tmp1 = np.max(tmp1)
    return tmp1 < 1


def get_converging_linear_system(A, F):
    A = np.copy(A)
    F = np.copy(F)

    B = A.transpose()

    F = np.dot(B, F)
    A = np.dot(B, A)

    return A, F


def solve(A, F, eps):
    if np.linalg.det(A) == 0:
        raise Exception("det(A) == 0")

    w = float(input("Input w: "))

    if w <= 0 or w >= 2:
        raise Exception("w must be: 0 < w < 2")

    A, F = get_converging_linear_system(A, F)

    x = np.zeros(F.size)

    norm_reversed_A = np.linalg.norm(np.linalg.inv(A))

    residual = np.dot(A, x) - F
    accuracy = norm_reversed_A * np.linalg.norm(residual)

    i = 0

    while accuracy >= eps:
        if i == MAX_ITERATION:
            print("Сходиться очень медленно i = ", i)
            break

        x = get_next(A, F, w, x)
        residual = np.dot(A, x) - F
        accuracy = norm_reversed_A * np.linalg.norm(residual)

        i += 1

    return x, i