def print_float_matrix(A, com=""):
    if com != '':
        print(com)

    for row in A:
        for val in row:
            print("{:13.10f}".format(val), end=' ')
        print()
    print()


def print_float_vector(A, com=""):
    if com != '':
        print(com)

    for val in A:
        print("{:13.10f}".format(val), end=' ')
    print('\n')
