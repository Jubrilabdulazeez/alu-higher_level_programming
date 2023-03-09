#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for j in range(len(matrix[i]))]
                  for i in range(len(matrix))]
    
    # Iterate through each element of the matrix and square its value
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
    
    # Return the new matrix with squared values
    return new_matrix
