from collections import deque
from math import floor
from functools import reduce

expression = input().split()

index = 0

function = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i])
}

while index < len(expression):
    element = expression[index]

    if element in "*/+-":
        result = function[element](index)
        [expression.pop(1) for i in range(index)]
        expression[0] = result
        index = 0
    index += 1

print(int(expression[0]))




# ujas tova dade 14 pointa pak ot skapania lektor
# haha = deque(input().split())
# idx = 0
#
# while idx < len(haha):
#     bobo = haha[idx]
#
#     if bobo in "/*+_":
#         for _ in range(idx - 1):
#             haha.appendleft(eval(f"{haha.popleft()} {bobo} {haha.popleft()}"))
#
#         del haha[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(haha[0])))




#tova smeshno ot lektora pak vze 85 tochki

# haha = deque(input().split())
# idx = 0
#
# while idx < len(haha):
#     bobo = haha[idx]
#
#     if bobo == '*':
#         for _ in range(idx - 1):
#             haha.appendleft(int(haha.popleft()) * int(haha.popleft()))
#     elif bobo == '/':
#         for _ in range(idx - 1):
#             haha.appendleft(int(haha.popleft()) / int(haha.popleft()))
#     elif bobo == '-':
#         for _ in range(idx - 1):
#             haha.appendleft(int(haha.popleft()) - int(haha.popleft()))
#     elif bobo == '+':
#         for _ in range(idx - 1):
#             haha.appendleft(int(haha.popleft()) + int(haha.popleft()))
#
#     if bobo in "/*+_":
#         del haha[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(haha[0])))


#tova e moeto reshenie keto vze 85 tochki
# line = input().split(' ')
# rez = 0
# haha = deque()
# haha2 = 0

# for x in line:
#     if x.isdigit():
#         haha.append(int(x))
#
#     if len(haha) > 1:
#         if x == "-":
#             for y in haha:
#                 if haha2 == 0:
#                     haha2 = y
#                 else:
#                     haha2 -= y
#             rez = haha2
#             haha.clear()
#         elif x == "+":
#             for y in haha:
#                 if haha2 == 0:
#                     haha2 = y
#                 else:
#                     haha2 += y
#             rez = haha2
#             haha.clear()
#         elif x == "*":
#             for y in haha:
#                 if haha2 == 0:
#                     haha2 = y
#                 else:
#                     haha2 *= y
#             rez = haha2
#             haha.clear()
#         elif x == "/":
#             for y in haha:
#                 if haha2 == 0:
#                     haha2 = y
#                 else:
#                     haha2 /= y
#             rez = floor(haha2)
#             haha2 = floor(haha2)
#             haha.clear()
#     else:
#         if x == "-":
#             for y in haha:
#                 haha2 -= y
#             rez = haha2
#             haha.clear()
#         elif x == "+":
#             for y in haha:
#                 haha2 += y
#             rez = haha2
#             haha.clear()
#         elif x == "*":
#             for y in haha:
#                 haha2 *= y
#             rez = haha2
#             haha.clear()
#         elif x == "/":
#             for y in haha:
#                 haha2 /= y
#             rez = floor(haha2)
#             haha2 = floor(haha2)
#             haha.clear()


# print(line)
# print(haha)
# print(haha2)
# print(abs(rez))


