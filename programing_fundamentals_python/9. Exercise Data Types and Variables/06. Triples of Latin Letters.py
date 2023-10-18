n = int(input())

for number in range(n):
    for number2 in range(n):
        for number3 in range(n):
            result = chr(97 + number)+chr(97 + number2)+chr(97 + number3)
            print(result)


#vtori vairant
#
# for number in range(1, n + 1):
#     for number2 in range(1, n + 1):
#         for number3 in range(1, n + 1):
#             result = chr(96 + number)+chr(96 + number2)+chr(96 + number3)
#             print(result)