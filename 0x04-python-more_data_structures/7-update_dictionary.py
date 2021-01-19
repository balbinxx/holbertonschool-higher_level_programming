#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    x = {key: value}
    a_dictionary.update(x)
    return (a_dictionary)


def print_sorted_dictionary(new_dict):
#imprimir dicts por elemento de forma "sort"
    for i in sorted(new_dict):   
        print("{}: {}".format(i, new_dict[i]))
