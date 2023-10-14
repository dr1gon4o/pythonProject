n = input()

x1 = 0
x2 = 0

while True:
    # n = input()
    if n == 'stop':
        break
    gemini = int(n)

    if gemini < 0:
        print("Number is negative.")
        n = input()
        continue

    count = 0

    for i in range(1, gemini + 1):
        if gemini % i == 0:
            count += 1

    if count == 2:
        x1 += gemini
    else:
        x2 += gemini
    n = input()


print(f"Sum of all prime numbers is: {x1}\n"
      f"Sum of all non prime numbers is: {x2}")
