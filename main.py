from solver.basic_math import calculate
from solver.tables import multiplication_table
from solver.statistics_solver import calculate_statistics
from solver.algebra import solve_math
from solver.matrices import (
    create_matrix,
    add_matrices,
    subtract_matrices,
    multiply_matrices,
    transpose_matrix,
    determinant,
    inverse_matrix,
    matrix_trace,
    input_matrix,
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
        while True:
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

            if matrix_choice == "1":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")

                try:
                    result = add_matrices(A, B)
                    print("\nResult:")
                    print(result)
                except Exception as e:
                    print("\nError:", e)

            elif matrix_choice == "2":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")

                try:
                    result = subtract_matrices(A, B)
                    print("\nResult:")
                    print(result)
                except Exception as e:
                    print("\nError:", e)

            elif matrix_choice == "3":
                A = input_matrix("Matrix A")
                B = input_matrix("Matrix B")

                try:
                    result = multiply_matrices(A, B)
                    print("\nResult:")
                    print(result)
                except Exception as e:
                    print("\nError:", e)

            elif matrix_choice == "4":
                A = input_matrix("Matrix")
                result = transpose_matrix(A)

                print("\nTranspose:")
                print(result)

            elif matrix_choice == "5":
                A = input_matrix("Matrix")

                try:
                    result = determinant(A)
                    print("\nDeterminant:")
                    print(result)
                except Exception as e:
                    print("\nError: Determinant requires a square matrix.")

            elif matrix_choice == "6":
                A = input_matrix("Matrix")

                try:
                    result = inverse_matrix(A)
                    print("\nInverse:")
                    print(result)
                except Exception as e:
                    print("\nError: Matrix cannot be inverted.")

            elif matrix_choice == "7":
                A = input_matrix("Matrix")

                try:
                    result = matrix_trace(A)
                    print("\nTrace:")
                    print(result)
                except Exception as e:
                    print("\nError: Trace requires a square matrix.")

            elif matrix_choice == "0":
                print("Returning to main menu...")
                break

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