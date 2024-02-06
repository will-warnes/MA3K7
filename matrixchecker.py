import numpy as np
import math

count_zero_det = 0
count_total_matrices = 0
count_start_with_zero = 0
count_zero_det_more_1s = 0
count_zero_det_more_0s = 0

def has_zero_determinant(matrix):
    global count_zero_det, count_zero_det_more_1s, count_zero_det_more_0s
    det = np.linalg.det(matrix)
    print(f"Matrix of size {len(matrix)}x{len(matrix[0])}: Determinant = {det}")
    if det == 0:
        print("Matrix has a zero determinant.")
        count_zero_det += 1
        total_ones = sum(sum(row) for row in matrix)
        if total_ones > len(matrix) * len(matrix[0]) / 2:
            count_zero_det_more_1s += 1
        elif total_ones < len(matrix) * len(matrix[0]) / 2:
            count_zero_det_more_0s += 1
    print_matrix(matrix)

def generate_all_matrices(n, m, matrix=None, row=0, col=0, start_with_zero=False):
    global count_total_matrices, count_start_with_zero
    if matrix is None:
        matrix = [[0] * m for _ in range(n)]

    if row == n:
        count_total_matrices += 1
        total_ones = sum(sum(row) for row in matrix)
        if (total_ones == math.floor((n * m) / 2) or total_ones == math.ceil((n * m) / 2)):
            has_zero_determinant(matrix)

        if start_with_zero and matrix[0][0] == 0:
            count_start_with_zero += 1

        return

    matrix[row][col] = 0
    next_row, next_col = (row, col + 1) if col + 1 < m else (row + 1, 0)
    generate_all_matrices(n, m, matrix, next_row, next_col, start_with_zero)

    matrix[row][col] = 1
    next_row, next_col = (row, col + 1) if col + 1 < m else (row + 1, 0)
    generate_all_matrices(n, m, matrix, next_row, next_col, start_with_zero)

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

n = 4  # change n for a different-sized matrix
generate_all_matrices(n, n, start_with_zero=True)
print(f"\nTotal matrices with zero determinant: {count_zero_det}")
print(f"Total matrices generated: {count_total_matrices}")
print(f"Total matrices that start with '0': {count_start_with_zero}")
print(f"Matrices with zero determinant and more 1s: {count_zero_det_more_1s}")
print(f"Matrices with zero determinant and more 0s: {count_zero_det_more_0s}")
