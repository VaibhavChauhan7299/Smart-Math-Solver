import sympy as sp


def add_matrices(matrix_a, matrix_b):
    return matrix_a + matrix_b


def multiply_matrices(matrix_a, matrix_b):
    return matrix_a * matrix_b


def matrix_determinant(matrix):
    return matrix.det()


def matrix_inverse(matrix):
    return matrix.inv()