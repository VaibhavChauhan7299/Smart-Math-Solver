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

if __name__ == "__main__":

    A = create_matrix([
        [1, 2],
        [3, 4]
    ])

    B = create_matrix([
        [5, 6],
        [7, 8]
    ])

    print("Matrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nAddition:")
    print(add_matrices(A, B))

    print("\nSubtraction:")
    print(subtract_matrices(A, B))

    print("\nMultiplication:")
    print(multiply_matrices(A, B))

    print("\nTranspose of A:")
    print(transpose_matrix(A))

    print("\nDeterminant of A:")
    print(determinant(A))

    print("\nInverse of A:")
    print(inverse_matrix(A))

    print("\nTrace of A:")
    print(matrix_trace(A))