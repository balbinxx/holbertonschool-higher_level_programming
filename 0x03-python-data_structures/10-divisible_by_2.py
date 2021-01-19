#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    siono = []
    for i in my_list:
        if i % 2 is 0:
            siono.append(True)
        else:
            siono.append(False)
    return siono
