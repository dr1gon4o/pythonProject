num = int(input())

for x in range(1, num +1):
    if num >= 1:
        num -= 1
        print("shooting...")
    if num == 0:
        print("no bullets left")

