#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda submat: list(map(lambda arg: arg**2, submat)), matrix))
