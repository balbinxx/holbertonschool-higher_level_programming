#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = (0, 0)
    tupla_ac = tuple_a + c
    tupla_bc = tuple_b + c
    return (tupla_ac[0] + tupla_bc[0], tupla_ac[1] + tupla_bc[1])
