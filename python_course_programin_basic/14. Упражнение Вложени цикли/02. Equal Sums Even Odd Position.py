x1 = int(input())
x2 = int(input())


for de in range(x1, x2 + 1):
    numbers_str = str(de)
    sumch = 0
    sumne = 0

    for index, digit in enumerate(numbers_str):
        if index % 2 == 0:
            sumch += int(digit)
        else:
            sumne += int(digit)

    if sumch == sumne:
        print(de, end=' ')

# tozi for e ot veronika
# for j in range(0, len(numbers_str)):
#     digit = int(numbers_str[j])
#     if j % 2 == 0:
#         sumch += digit
#     else:
#         sumne += digit
