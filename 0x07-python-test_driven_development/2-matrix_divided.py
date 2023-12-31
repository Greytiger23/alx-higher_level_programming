#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(isinstance(row, list) and all(isinstance(element,
    (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    a = [[round(element / div, 2) for element in row] for row in matrix]
    return a

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
