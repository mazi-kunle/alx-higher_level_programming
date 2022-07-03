#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0 orr idx > len(my_list)):
        return (my_list)
    new_list = my_list
    my_list[idx] = element
    return new_list
