#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    for b in range(len(matrix)):
        for c in range(len(matrix[0])):
            a[b][c] = matrix[b][c] ** 2
    return a
