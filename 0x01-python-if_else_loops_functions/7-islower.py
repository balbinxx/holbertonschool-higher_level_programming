#!/usr/bin/python3
def islower(c):
    x = ord(c)
    while x >= 97 and x <= 122:
        return True
    else:
        return False
