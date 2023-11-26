
# def char(x1=input(), x2=input()):
#     for i in range(ord(x1), ord(x2)):
#         if i == ord(x2) - 1:
#             break
#
#         print(chr(i+1), end=' ')


x1 = input()
x2 = input()

for i in range(ord(x1), ord(x2)):
    if i == ord(x2) - 1:
        break

    print(chr(i+1), end=' ')

# print(char())
