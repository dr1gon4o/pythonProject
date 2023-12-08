income = float(input())
num_user = int(input())
# num_search = int(input())

smetka = 0
total = 0

for x in range(1, num_user + 1):
    nums = int(input())
    total = nums * income

    if nums > 5:
        total = total * 2
        # smetka += total
    if nums == 1:
        continue
    if x % 3 == 0:
        # total = total * 3
        if nums > 5:
            total = nums * (income * 2)
            total = total * 3
        elif nums == 1:
            pass
        else:
            total = total * 3

    smetka += total


print(f"Total money earned: {smetka:.2f}")