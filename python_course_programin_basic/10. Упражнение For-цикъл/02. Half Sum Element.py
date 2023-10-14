import os
import sys

n = int(input())

max = -sys.maxsize
sum = 0

for i in range(0, n):
    x = int(input())
    if x > max:
        max = x
    sum += x

sum = sum - max
diff = abs(max - sum)

if max == sum:
    print(f"Yes", f"Sum = {sum}", sep=os.linesep)
else:
    print(f"No", f"Diff = {diff}", sep=os.linesep)
    