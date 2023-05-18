#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = [[0 for a in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sq[i][j] = matrix[i][j] ** 2

    return sq
