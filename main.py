from solver.basic_math import calculate
from solver.tables import multiplication_table
from solver.statistics import calculate_statistics
from solver.algebra import solve_math
from solver.matrices import (
    create_matrix,
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    transpose_matrix,
    determinant,
    inverse_matrix,
    matrix_trace
)

print("========== AI MATH SOLVER ==========")

while True:

    print("\n1. Basic Calculator")
    print("2. Multiplication Table")
    print("3. Statistics")
    print("4. Matrix")
    print("5. Graph")
    print("6. Algebra")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        expression = input("Enter expression: ")

        answer = calculate(expression)

        print("\nExpression:", expression)
        print("Answer:", answer)

    elif choice == "2":

        number = int(input("Enter number: "))
        limit = int(input("Enter ending number: "))

        table = multiplication_table(number, limit)

        for line in table:
            print(line)

    elif choice == "3":

        values = input("Enter numbers separated by spaces: ")

        numbers = [float(x) for x in values.split()]

        result = calculate_statistics(numbers)

        print(result)

    elif choice == "4":

        print("\n========== MATRIX SOLVER ==========")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Inverse")
        print("7. Trace")
        print("0. Back")

        matrix_choice = input("\nEnter your choice: ")

        A = create_matrix([
            [1, 2],
            [3, 4]
        ])

        B = create_matrix([
            [5, 6],
            [7, 8]
        ])

        if matrix_choice == "1":

            print("\nMatrix A + Matrix B:")
            print(add_matrices(A, B))

        elif matrix_choice == "2":

            print("\nMatrix A - Matrix B:")
            print(subtract_matrices(A, B))

        elif matrix_choice == "3":

            print("\nMatrix A × Matrix B:")
            print(multiply_matrices(A, B))

        elif matrix_choice == "4":

            print("\nTranspose of Matrix A:")
            print(transpose_matrix(A))

        elif matrix_choice == "5":

            print("\nDeterminant of Matrix A:")
            print(determinant(A))

        elif matrix_choice == "6":

            print("\nInverse of Matrix A:")
            print(inverse_matrix(A))

        elif matrix_choice == "7":

            print("\nTrace of Matrix A:")
            print(matrix_trace(A))

        elif matrix_choice == "0":

            print("Returning to main menu...")

        else:

            print("Invalid matrix choice.")


    elif choice == "5":

        print("Graph Solver Coming Soon...")

    elif choice == "6":

        print("\n========== ALGEBRA SOLVER ==========")

        algebra_problem = input("Enter algebra problem: ")

        result = solve_math(algebra_problem)

        print("\nResult:", result)

    elif choice == "0":

        print("Thank you for using AI Math Solver.")
        break

    else:

        print("Invalid choice.")