#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    # create a new matrix with the same size as the input matrix
    result = [[0 for j in range(num_cols)] for i in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_cols):
            result[i][j] = matrix[i][j] *
    return result
