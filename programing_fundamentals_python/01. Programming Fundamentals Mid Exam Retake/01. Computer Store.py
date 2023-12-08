num = input()

total = 0
# tax = total * 0.2
# final = total + tax

while True:
    # nam = float(num)
    if num == "special" or num == "regular":
        break
    num = float(num)
    if num < 0:
        print("Invalid price!")
    else:
        total += num

    num = input()

tax = total * 0.2
final = total + tax

if total > 0:
    if num == "special":
        final = final - (final * 0.1)
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total:.2f}$\nTaxes: {tax:.2f}$"
              f"\n -----------\nTotal price: {final:.02f}$")
    else:
        print(
            f"Congratulations you've just bought a new computer!\nPrice without taxes: {total:.2f}$\nTaxes: {tax:.2f}$"
            f"\n -----------\nTotal price: {final:.02f}$")
else:
    print("Invalid order!")

