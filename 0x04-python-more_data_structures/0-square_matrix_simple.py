#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix[:]
    for i in range(len(new)):
        new[i] = list(map(square, new[i]))
    return new
def square(x):
    return x ** 2
