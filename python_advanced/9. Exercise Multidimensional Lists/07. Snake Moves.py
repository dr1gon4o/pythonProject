from collections import deque


x, y = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)

for row in range(x):
    while len(word_copy) < y:
        word_copy.extend(word)

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(y)], sep="")
    else:
        print(*[word_copy.popleft() for _ in range(y)][::-1], sep="")
















# tova e moito deto ne rboti dobre:
# x, y = [int(el) for el in input().split()]
# mat = []
#
# line = input()
#
# for z1 in range(x):
#     haha = deque()
#     haha2 = deque()
#     for z2 in line:
#         if len(mat) % 2 == 0:
#             if len(haha) < y:
#                 haha.append(z2)
#             if len(haha) == y:
#                 mat.append(haha)
#             continue
#         elif len(mat) % 2 != 0:
#             if len(haha2) < y:
#                 haha2.appendleft(z2)
#             if len(haha2) == y:
#                 mat.append(haha2)
#             continue
#
#         if len(mat) == x:
#             break

# print(x, y)
# print(*mat)
# [print(*el) for el in mat]
# print(line)

