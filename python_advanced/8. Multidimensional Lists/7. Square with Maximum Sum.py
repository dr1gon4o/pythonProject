
x, y = [int(el) for el in (input().split(","))]

mat = []

for o in range(x):
    # haha = [int(el) for el in (input().split(","))]
    # mat.append(haha)
    mat.append([int(el) for el in (input().split(","))])

# red1 = []
# red2 = []
# haha1, haha2 = 0, 0
malka_2x2 = []

max_sum = float("-inf")
# hoho = 0

for z1 in range(x-1):
    for z2 in range(y-1):
        haha1 = mat[z1][z2]
        haha2 = mat[z1][z2+1]
        haha3 = mat[z1+1][z2]
        haha4 = mat[z1+1][z2+1]
        bobo = haha1 + haha2 + haha3 + haha4
        # if bobo > hoho:
        #     hoho = bobo

        if max_sum < bobo:
            max_sum = bobo
            malka_2x2 = [[haha1, haha2],[haha3, haha4]]

        # if mat[z1] and mat[z1][z2] > haha1 and haha2:
        #     haha1, haha2 = mat[z1], mat[z1][z2]
        #     red1.append(haha1 + haha2)




# print(x,y)
# print(mat)
# # print(red1)
# print(mat[1][2])
# print(mat[1])

# print(*malka_2x2, sep='\n')
print(*malka_2x2[0])
print(*malka_2x2[1])
print(max_sum)

