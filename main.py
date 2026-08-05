from solver.basic_math import calculate
from solver.tables import multiplication_table
from solver.statistics import calculate_statistics

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

        print("Matrix Solver Coming Soon...")

    elif choice == "5":

        print("Graph Solver Coming Soon...")

    elif choice == "6":

        print("Algebra Solver Coming Soon...")

    elif choice == "0":

        print("Thank you for using AI Math Solver.")
        break

    else:

        print("Invalid choice.")