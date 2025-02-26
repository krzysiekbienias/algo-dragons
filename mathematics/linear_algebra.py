from typing import List


class MatrixTraverse:
    def __init__(self, matrix: List[List[int]] = None):
        self.__matrix = matrix if matrix is not None else [[]]

    def get_matrix(self) -> List[List[int]]:
        """Getter method for the matrix attribute."""
        return self.__matrix

    def set_matrix(self, new_matrix: List[List[int]]):
        """Setter method for the matrix attribute."""
        if not isinstance(new_matrix, list) or not all(isinstance(row, list) for row in new_matrix):
            raise ValueError("Matrix must be a list of lists.")
        self.__matrix = new_matrix  # Update the private attribute

    def row_by_row(self) -> List[int]:
        result = []
        start_row, end_row = 0, len(self.__matrix) - 1
        start_col, end_col = 0, len(self.__matrix[0]) - 1
        while start_row <= end_row and start_col <= end_col:
            for col in range(start_col, end_col + 1):
                result.append(self.__matrix[start_row][col])
            start_row += 1
        return result

    def column_by_column(self) -> List[int]:
        result = []
        start_row, end_row = 0, len(self.__matrix) - 1
        start_col, end_col = 0, len(self.__matrix[0]) - 1
        while start_row <= end_row and start_col <= end_col:
            for row in range(start_row, end_row + 1):
                result.append(self.__matrix[row][start_col])
            start_col += 1
        return result

    def snake(self):
        pass

    def spiral(self):
        pass

def matrix_multiplication(mat_a, mat_b):
    # remember that we need 3 loops to multiply
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

    # matrix_a = np.arrays([[0, 2, 0], [0, 0, 0], [0, 0, 0]])
    # matrix_b = np.arrays([[0, 0, 0], [0, 1, 0], [0, 0, 3]])
    # sparce_matrix(matrix_a, matrix_b)
