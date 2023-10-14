n = int(input())

sum = 0

for _ in range(1, n + 1):
    x = int(input())
    sum = sum + x

sum2 = 0

for _ in range(1, n + 1):
    x = int(input())
    sum2 = sum2 + x

if sum == sum2:
    print(f"Yes, sum = {sum}")
else:
    diff = abs(sum2 - sum)
    print(f"No, diff = {diff}")
