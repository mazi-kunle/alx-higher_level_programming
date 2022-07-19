#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    index = 0
    if (list_length <= 0):
        print("out of range")
        return new_list

    while True:
        try:
            if (index < list_length):
                result = my_list_1[index] / my_list_2[index]
                new_list.append(result)
            else:
                return new_list
        except (TypeError):
            result = 0
            print("wrong type")
            new_list.append(result)
        except (ZeroDivisionError):
            result = 0
            print("division by 0")
            new_list.append(result)
        except (IndexError):
            result = 0
            print("out of range")
            new_list.append(result)
        finally:
            index = index + 1
