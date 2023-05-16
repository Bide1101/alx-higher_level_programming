#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    length = len(my_list) - 1
    if idx > 0 and idx < length:
        new_list = my_list[:]
        for i in range(length):
            if i == idx:
                new_list[i] = element
                return new_list
    else:
        return my_list
