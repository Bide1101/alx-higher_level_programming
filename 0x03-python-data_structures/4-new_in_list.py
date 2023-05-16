#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if idx > 0 and idx < length:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
    else:
        return my_list
