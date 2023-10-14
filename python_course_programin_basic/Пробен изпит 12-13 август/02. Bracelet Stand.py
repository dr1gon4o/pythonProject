x = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())


spesteni = x * 5
# razhod_naden = x3 / 5
obsh_pechalba = x2 * 5
x5 = (spesteni + obsh_pechalba) - x3


if x5 >= x4:
    print(f"Profit: {x5:.02f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {x4 - x5:.02f} BGN.")
