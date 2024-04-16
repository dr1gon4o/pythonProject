
x, y = [int(el) for el in input().split()]

mat = [el for el in range(x) for el in [input().split()]]

num = 0

for z1 in range(x-1):
    for z2 in range(y-1):
        haha1 = mat[z1][z2]
        haha2 = mat[z1][z2+1]
        haha3 = mat[z1+1][z2]
        haha4 = mat[z1+1][z2+1]

        if haha4 == haha3 == haha2 == haha1:
            num += 1



# print(x, y)
# print(mat)
print(num)
