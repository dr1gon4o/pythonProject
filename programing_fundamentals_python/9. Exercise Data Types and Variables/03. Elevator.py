from math import ceil

p = int(input())
n = int(input())

course = p // n
if p % n != 0:
    course += 1

print(course)


# vtori variant
# course = ceil(p / n)
#
# print(course)