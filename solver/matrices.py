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