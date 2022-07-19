#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    count = 0
    while True:
        try:
            if (index < x):
                print("{:d}".format(my_list[index]), end='')
                count = count + 1
                index = index + 1
            elif (x == index):
                print()
                return count
        except (ValueError, TypeError):
            index = index + 1
            continue
