#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if (len(sys.argv) != 4):
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)

    if (sys.argv[2] not in '+-*/'):
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    lst = [(add, '+'), (sub, '-'), (mul, '*'), (div, '/')]
    for i in lst:
        if (i[1] == sys.argv[2]):
            result = i[0](int(sys.argv[1]), int(sys.argv[3]))
    print('{} <{}> {} = {}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        result))
