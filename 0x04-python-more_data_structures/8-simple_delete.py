#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        a_dictionary.pop(key)
        return(a_dictionary)
    else:
        return(a_dictionary)


def print_sorted_dictionary(new_dict):
    for i in sorted(new_dict):
        print("{}: {}".format(i, new_dict[i]))
