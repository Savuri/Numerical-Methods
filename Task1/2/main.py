import read
import calc
import output

eps = 1.0e-08

if __name__ == '__main__':
    A, F = read.input_data_of_problem()

    x, i = calc.solve(A, F, eps)

    output.print_float_vector(x, "Solution: ")
    print("Iterations = ", i)
