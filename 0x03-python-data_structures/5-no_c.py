#!/usr/bin/python3
def no_c(my_string):
    x = ("c", "C")
    new = ""
    for nc in my_string:
        if nc not in x:
            new += nc
    return new
