import string
eggs = list(string.ascii_lowercase)


x,y = [int(el) for el in input().split()]
# mat = []

for z1 in range(x):
    list = []

    for z2 in range(y):

        malk_list = eggs[z1]+eggs[z1+z2]+eggs[z1]
        list.append(malk_list)
        # mat.append(malk_list)
    print(*list, sep=" ")

# print(x)
# print(y)
# print(eggs)
# print(*list, sep=" ")
# print(*mat, sep=" ")




# tova e vtori variant kato rechenie!
#
# rows, cols = [int(x) for x in input().split()]
#
# start = ord('a')
#
# for row in range(start, start + rows):
#     for col in range(row, row + cols):
#         print(chr(row), chr(col), chr(row), sep="", end=" ")
#
#     print()