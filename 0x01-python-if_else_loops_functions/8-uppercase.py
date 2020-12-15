#!/usr/bin/python3
def uppercase(str):
    for i in str:
        aux = ord(i)
        if aux > 96 and aux < 123:       
            aux -= 32
        print('{:c}'.format(aux), end='')
    print(end='\n')
