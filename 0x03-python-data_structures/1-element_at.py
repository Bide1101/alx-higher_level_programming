#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx >= 0 and idx < length:
        for i in my_list:
            if i == idx:
                return my_list[i]
    else:
        return None
