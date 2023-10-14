num = int(input())

for x in range(1, num + 1):
    for j in range(0, x):
        print("*", end='')
    print()
for x in range(num - 1, 0, - 1):
    for j in range(0, x):
        print("*", end='')
    print()
