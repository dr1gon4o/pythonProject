num = float(input())

while True:
    if 1 <= num <= 100:
        print(f"The number {num} is between 1 and 100")
        break
    else:
        num = float(input())
