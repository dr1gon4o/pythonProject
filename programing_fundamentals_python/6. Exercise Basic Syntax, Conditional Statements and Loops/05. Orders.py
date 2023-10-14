orders = int(input())

total = 0

for x in range(orders):
    caps_price = float(input())
    days = int(input())
    caps = int(input())

    if (0.01 <= caps_price <= 100) and (1 <= days <= 31) and (1 <= caps <= 2000):
        price = caps_price * caps * days
        total += price
        print(f"The price for the coffee is: ${price:.2f}")
    else:
        continue


print(f"Total: ${total:.2f}")
