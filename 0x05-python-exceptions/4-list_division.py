#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lista = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            lista.append(div)
            div = 0   
    return lista
