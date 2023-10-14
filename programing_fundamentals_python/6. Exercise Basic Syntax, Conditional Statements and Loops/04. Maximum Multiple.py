divisor = int(input())
boundary = int(input())

number = 0

for x in range(boundary + 1):
    if (x % divisor == 0) and (x <= boundary) and (x > 0):
        number = x

print(number)
