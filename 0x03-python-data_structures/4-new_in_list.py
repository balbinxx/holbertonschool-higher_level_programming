#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    aux = my_list.copy()
    if idx < 0 or idx + 1 > len(aux):
        return aux
    else:
        aux[idx] = element
        return aux
