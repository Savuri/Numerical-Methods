from math import sin
import numpy as np
import output

norm = 1
BIG_NUMBER = 1000000

def read_from_file():
    test_number = 0

    while test_number != 1 and test_number != 2 and test_number != 3 and test_number != 4:
        test_number = int(input("Which example should i test (4 - custom): "))

    if (test_number == 4):
        print("input your custom input in ./tests/4.txt in format: first number is n, next n * n numbers - A, last n "
              "number - f")

    file = open("./tests/" + str(test_number) + ".txt", "r")

    numbers_pull = np.array(list(map(float, file.read().split())))

    n = int(numbers_pull.item(0))
    numbers_pull = np.delete(numbers_pull, 0, 0)

    A = np.empty((n, n))

    for i in range(n):
        for j in range(n):
            A[i][j] = numbers_pull.item(0)
            numbers_pull = np.delete(numbers_pull, 0, 0)

    F = np.empty((n))

    for i in range(n):
        F[i] = numbers_pull.item(0)
        numbers_pull = np.delete(numbers_pull, 0, 0)

    if (np.max(A) > BIG_NUMBER or np.max(F) > BIG_NUMBER):
        print("Matrix A or vector F has element greater then",  BIG_NUMBER, "\n. They were normalized")

        global norm
        if (np.max(A) > BIG_NUMBER):
            norm = np.linalg.norm(A)
        else:
            norm = np.linalg.norm(A)

        A /= norm
        F /= norm

        mode = '0'
        while mode.lower() != 'y' and mode.lower() != 'n':
           mode = input("Do you want to see normalized A and F?(Y or N): ")

        if (mode.lower() == 'y'):
            print("norm:\n", norm, "\n")
            output.print_float_matrix(A, "normalized A:")
            output.print_float_vector(F, "normalized F:")

    return A, F


def read_as_formula():
    n = 40

    print("My formula: example 2-2")
    m = 2

    q = 1.001 - 2 * m * 10 ** (-3)

    A = np.empty((n, n))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                A[i - 1][j - 1] = q ** (i + j) + 0.1 * (j - i)
            else:
                A[i - 1][j - 1] = (q - 1) ** (i + j)

    x = float(input("Input x = "))

    F = np.empty(n)

    for i in range(1, n):
        F[i - 1] = abs(x - n / 10) * i * sin(x)

    return A, F


def input_data_of_problem():
    mode = int(input("Mode (1 - matrix from example or custom matrix, 2 - matrix formula) = "))

    while mode != 1 and mode != 2:
        print("Wrong mode")
        mode = int(input("Mode (1- matrix from example or custom matrix, 2 - matrix formula) = "))

    if (mode == 1):
        return read_from_file()
    else:
        return read_as_formula()