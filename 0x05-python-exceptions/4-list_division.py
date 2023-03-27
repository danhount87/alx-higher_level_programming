#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for j in range(0, list_length):
        try:
            dvn = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            dvn = 0
        except ZeroDivisionError:
            print("division by 0")
            dvn = 0
        except IndexError:
            print("out of range")
            dvn = 0
        finally:
            new_list.append(dvn)
    return (new_list)
