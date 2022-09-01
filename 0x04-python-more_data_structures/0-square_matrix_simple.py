#!/usr/bin/python3

def squared_list(a_list):
    a = lambda x:x**2
    return list(map(a, a_list))

def square_matrix_simple(matrix=[]):
    matrixCopy = matrix[:]
    return list(map(squared_list, matrixCopy))
