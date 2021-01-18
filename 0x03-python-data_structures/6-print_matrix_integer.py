#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for filas in matrix:
            for colum in filas:
                print("{:d}".format(colum), end="")
                if colum != filas[-1]:
                    print(" ", end="")
            print()
