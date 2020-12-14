#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if i < x and (i != 8 or x != 9):
                print('{}{}, '.format(i, x), end='')
        if i == 8 and x == 9:
            print('{}{}'.format(i, x))
