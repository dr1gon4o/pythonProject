import sys
import os

n = int(input())

max = -sys.maxsize
min = sys.maxsize

for _ in range(n):
    x = int(input())
    if x > max:
        max = x
    if x < min:
        min = x

print(f"Max number: {max}", f"Min number: {min}", sep=os.linesep)
