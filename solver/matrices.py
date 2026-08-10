from sympy import Matrix


def create_matrix(data):
    """Create a SymPy matrix from a list of lists."""
    return Matrix(data)


def add_matrices(matrix_a, matrix_b):
    """Add two matrices."""
    return matrix_a + matrix_b


def subtract_matrices(matrix_a, matrix_b):
    """Subtract matrix B from matrix A."""
    return matrix_a - matrix_b


def multiply_matrices(matrix_a, matrix_b):
    """Multiply two matrices."""
    return matrix_a * matrix_b


def transpose_matrix(matrix):
    """Return the transpose of a matrix."""
    return matrix.T


def determinant(matrix):
    """Calculate the determinant."""
    return matrix.det()


def inverse_matrix(matrix):
    """Calculate the inverse of a matrix."""
    return matrix.inv()


def matrix_trace(matrix):
    """Calculate the trace of a matrix."""
    return matrix.trace()


def input_matrix(name):
    """Get a matrix from the user."""

    print(f"\nEnter {name}")

    # Ask user for dimensions
    rows = int(input("Number of rows: "))
    columns = int(input("Number of columns: "))

    data = []

    # Ask user for every row
    for i in range(rows):

        while True:

            values = input(
                f"Row {i + 1} ({columns} numbers): "
            ).split()

            # Check number of values
            if len(values) != columns:
                print(
                    f"Please enter exactly {columns} numbers."
                )
                continue

            try:

                row = [float(value) for value in values]

                data.append(row)

                break

            except ValueError:

                print("Please enter valid numbers.")

    return Matrix(data)


if __name__ == "__main__":

    print("========== MATRIX TEST ==========")

    A = input_matrix("Matrix A")

    print("\nMatrix A:")
    print(A)

    print("\nDeterminant:")
    
    if A.rows == A.cols:
        print(determinant(A))
    else:
        print("Determinant requires a square matrix.")

    print("\nTranspose:")
    print(transpose_matrix(A))