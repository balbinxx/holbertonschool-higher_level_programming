#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for i in new:
        new[i] = a_dictionary[i] * 2
    return (new)


def print_sorted_dictionary(new_dict):
    for i in sorted(new_dict):
        print("{}: {}".format(i, new_dict[i]))
