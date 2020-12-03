import numpy as np

MAX_ITERATION = 1000000000


def get_next(B, c, x):
    return np.dot(B, x) + c


def criteria(B):
    tmp1, _ = np.linalg.eig(B)
    tmp1 = tmp1.astype(complex)
    tmp1 = np.abs(tmp1)
    tmp1 = np.max(tmp1)
    return tmp1 < 1


def get_converging_linear_system(A, F):
    A = np.copy(A)
    F = np.copy(F)

    F = np.dot(A.transpose(), F)
    A = np.dot(A.transpose(), A)

    return A, F


def solve(A, F, eps):
    if np.linalg.det(A) == 0:
        raise Exception("det(A) == 0")

    w = float(input("Input w: "))

    if w <= 0 or w >= 2:
        raise Exception("w must be: 0 < w < 2")

    A, F = get_converging_linear_system(A, F)

    A_diag  = np.diag(np.diag(A))
    A_lower = np.tril(A) - A_diag
    A_upper = np.triu(A) - A_diag

    B = -np.dot(np.linalg.inv(1 / w * A_diag + A_lower),
                (1 - 1 / w) * A_diag + A_upper)
    c = np.dot(np.linalg.inv(1 / w * A_diag + A_lower), F)

    x = np.zeros(F.size)

    if not criteria(B):
        raise Exception("Criteria wrong!")

    norm_reversed_A = np.linalg.norm(np.linalg.inv(A))

    residual = np.dot(A, x) - F
    accuracy = norm_reversed_A * np.linalg.norm(residual)

    i = 0

    while accuracy >= eps:
        if i == MAX_ITERATION:
            print("Сходиться очень медленно i = ", i)
            break

        x = get_next(B, c, x)
        residual = np.dot(A, x) - F
        accuracy = norm_reversed_A * np.linalg.norm(residual)

        i += 1

    return x, i