from typing import List

import numpy as np


def matrix_multiplication(mat_a, mat_b):
    c = [[0] * len(mat_b[0]) for _ in range(len(mat_a))]
    for i in range(len(mat_a)):
        for j in range(len(mat_b[0])):
            for k in range(len(mat_a[0])):
                c[i][j] += mat_a[i][k] * mat_b[k][j]
    return c


def sparce_matrix(matrix_a, matrix_b=None):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    non_zero_a: dict = get_non_zero_elements_dict(matrix_a)
    non_zero_b: dict = get_non_zero_elements_dict(matrix_b)
    matrix_c: list = [[0] * len(non_zero_b) for _ in range(len(matrix_a))]
    for i, k in non_zero_a.keys():
        for j in range(len(matrix_b[0])):
            if (k, j) in non_zero_b.keys():
                matrix_c[i][j] += non_zero_a[(i, k)] * non_zero_b[(k, j)]
    return matrix_c


def get_non_zero_elements_dict(a_matrix: List[List[int]]) -> dict:
    """
    Description
    -----------
    This function takes a matrix as input and returns a dictionary that contains only non-zero elements.

    Parameters
    ----------
    a_matrix

    Returns
    -------
    Dictionary that contains only non-zero elements, from matrix.

    """

    non_zero_cells_dict = dict()
    for i in range(len(a_matrix)):
        for j in range(len(a_matrix[0])):
            if a_matrix[i][j] != 0:
                non_zero_cells_dict[(i, j)] = a_matrix[i][j]
    return non_zero_cells_dict


def transpose_matrix(matrix):
    transposed_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transpose_matrix


if __name__ == '__main__':
    matrix_a = [[2, 1, 3], [3, 4, 1]]
    matrix_b = [[1, 2, 0, 4], [1, -1, 3, 5], [2, 0, 1, 8]]
    transpose_matrix(matrix_a)
    matrix_c = matrix_multiplication(matrix_a, matrix_b)

    # matrix_a = np.array([[0, 2, 0], [0, 0, 0], [0, 0, 0]])
    # matrix_b = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 3]])
    # sparce_matrix(matrix_a, matrix_b)
