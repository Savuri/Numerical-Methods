import read
import output
import calc

from numpy import linalg as lg

if __name__ == '__main__':
    A, F = read.input_data_of_problem()

    output.print_float_vector(lg.solve(A, F) + 1)
    mode = 0
    while mode < 1 or mode > 5:
        mode = int(input("What should i calculate? (1 - determinate, 2 - Invertible matrix, 3 - Conditional number, \n"
                  "4 - solve linear equation without choosing main element, 5 - solve linear equation with "
                  "choosing main element)\n"))
        if (mode == 1):
            print("Determinate(A) = " + str(calc.det(A) * read.norm ** A[0].size) + '\n')
            break
        elif (mode == 2):
            output.print_float_matrix(calc.inverse_matrix(A) / read.norm, "Inverse Matrix")
            break
        elif (mode == 3):
            print("Conditional number = " + str(calc.conditional_number(A * read.norm)) + '\n')
            break
        elif (mode == 4):
            output.print_float_vector(calc.solve(A, F, False), "Solution:")
            break
        elif (mode == 5):
            output.print_float_vector(calc.solve(A, F, True), "Solution with main element:")
            break
