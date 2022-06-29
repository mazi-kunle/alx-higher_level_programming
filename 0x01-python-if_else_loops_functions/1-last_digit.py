#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = str(number)[-1] if number > 0 else str(-1 * int(str(number)[-1]))
print("Last digit of", number, "is", last_num, end=" ")
if (int(last_num) > 5):
    print("and is greater than 5")
elif (int(last_num) == 0):
    print("and is 0")
elif (int(last_num) < 6 or number < 0):
    print("and is less than 6 and not 0")

