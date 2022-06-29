#!/usr/bin/python3
flag = 0
for i in range(122, 96, -1):
    print(f'{chr(i - flag)}', end='')
    if (flag == 0):
        flag = 32
    else:
        flag = 0
