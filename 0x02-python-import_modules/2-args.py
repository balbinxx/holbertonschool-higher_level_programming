#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x_len = len(sys.argv)
    if x_len == 1:
        print('{:d} arguments.'.format(x_len - 1))
    elif x_len == 2:
        print('{:d} argument:'.format(x_len - 1))
        for i in range(x_len):
            if i != 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
    else:
        print("{:d} arguments:".format(x_len - 1))
        for i in range(x_len):
            if i != 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
