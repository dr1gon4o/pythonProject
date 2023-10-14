import math
import sys

year = int(input())
new_number = 0
for digit in range(year, sys.maxsize):
    number = str(digit)
    # new_number = 0
    if number[0] != number[1] and number[2] and number[3]\
            or number[1] != number[0] and number[2] and number[3]\
            or number[2] != number[1] and number[0] and number[3]\
            or number[3] != number[1] and number[2] and number[0]:
        new_number = number
        break
print(new_number)
