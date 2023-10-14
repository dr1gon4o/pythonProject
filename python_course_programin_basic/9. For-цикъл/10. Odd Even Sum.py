import os

n = int(input())

sum = 0
gg = 0

for x3 in range(1, n + 1):
    x = int(input())
    if x3 % 2 == 0:
        sum += x
    else:
        gg += x

if sum == gg:
    print(f"Yes", f"Sum = {sum}", sep=os.linesep)
else:
    diff = abs(gg - sum)
    print(f"No", f"Diff = {diff}", sep=os.linesep)
