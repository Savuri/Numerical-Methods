import numpy as np


def det(A):
    A = A.copy()

    if (A[:, 0].size != A[0].size) :
        raise Exception('Matrix is not square')
    n = A[:, 0].size
    sign = 0
    det = 1

    for i in range(n):
        shift = 0

        while i + shift < n and A[i + shift][i] == 0:
            shift += 1

        if i + shift >= n:
            return 0
        elif shift != 0:
            A[i], A[i + shift] = np.copy(A[i + shift]), np.copy(A[i])
            sign += 1

        switch_index = i
        for j in range(i + 1, n):
            if abs(A[i][j]) > abs(A[i][i]):
                switch_index = j

        if switch_index != i:
            sign += 1
            A[:, i], A[:, switch_index] = np.copy(A[:, switch_index]), np.copy(A[:, i])


        det *= A[i][i]
        A[i] /= A[i][i]

        for j in range(i + 1, n):
            A[j] -= A[j][i] * A[i]

    for i in range(n):
        det *= A[i][i]

    if (sign % 2 == 1):
        det *= -1


    return det


def inverse_matrix(A):
    A = A.copy()
    if (det(A) == 0):
        raise Exception("det(A) == 0")

    E = np.eye(A[0].size)
    A = np.hstack((A, E))
    ORDER = forward_elimination(A, True)
    back_substitution(A)
    A = A[:, A[0].size // 2:]
    ORDER = ORDER[:, 0]
    ORDER.shape = (A[0].size, 1)
    ORDER.shape = (A[0].size, 1)
    B = np.hstack((A, ORDER))
    B = B[B[:, A[0].size].argsort()]
    A = B[:, :A[0].size]

    return A


def conditional_number(A):
    B = inverse_matrix(A)

    return np.linalg.norm(B) * np.linalg.norm(A)


def create_extended_matrix(A, F):
    F.shape = (A[0].size, 1)
    B = np.hstack((A, F))
    F.shape = (A[0].size)

    return B


def forward_elimination(A, with_main_elem):
    n = A[:, 0].size
    ORDER = np.empty((n, 2))

    for i in range(n):
        ORDER[i][0] = i

    for i in range(n):
        shift = 0

        while i + shift < n and A[i + shift][i] == 0:
            shift += 1

        if i + shift >= n:
            raise Exception('Det(A) = 0')
        elif shift != 0:
            A[i], A[i + shift] = np.copy(A[i + shift]), np.copy(A[i])

        if (with_main_elem):
            switch_index = i
            for j in range(i + 1, n):
                if abs(A[i][j]) > abs(A[i][i]):
                    switch_index = j

            if switch_index != i:
                A[:, i], A[:, switch_index] = np.copy(A[:, switch_index]), np.copy(A[:, i])
                ORDER[i], ORDER[switch_index] = np.copy(ORDER[switch_index]), np.copy(ORDER[i])

        A[i] /= A[i][i]

        for j in range(i + 1, n):
            A[j] -= A[j][i] * A[i]
    return ORDER


def back_substitution(A):
    n = A[:, 0].size

    for i in range(n - 1, -1, -1):
        for j in range(i):
            A[j] -= A[i] * A[j][i]

    return


def solve(A, F, with_main_element):
    if det(A) == 0:
        raise Exception("det(A) == 0")

    B = create_extended_matrix(A, F)
    X_WITH_ORDER = forward_elimination(B, with_main_element)
    back_substitution(B)

    for i in range(A[0].size):
        X_WITH_ORDER[i][1] = B[i][A[0].size]


    X_WITH_ORDER = X_WITH_ORDER[X_WITH_ORDER[:, 0].argsort()]
    X = X_WITH_ORDER[:, 1]

    return X