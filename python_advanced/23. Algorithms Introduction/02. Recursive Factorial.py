num = int(input())

res = 1
for x in range(num, 0, -1):
    res *= x

print(res)


#vtori variant moi
#
# def frakt(num):
#     res = 1
#     for x in range(num, 0, -1):
#         res *= x
#     return res
#
# num = int(input())
# print(frakt(num))


#ednakvi sa variantite (vurshat sushtata rabota)

#treti variant kakto v lekciata (recurtion) vij returna
#
# def get_factorial(n: int):
#     if n == 0:
#         return 1
#
#     return n * get_factorial(n - 1)
#
#
# n = int(input())
# print(get_factorial(n))

