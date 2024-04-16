
x, y = [int(el) for el in input().split()]

# mat = [int(el) for el in range(x) for r in [input().split()]]
# mat = [[int(el) for i in (input().split())] for r in range(x)]

mat = []

for i in range(x):
    mat.append([int(el) for el in (input().split())])

mati = []
summ = 0
max_sum = float("-inf")

for z1 in range(x-2):
    for z2 in range(y-2):
        haha1 = mat[z1][z2]
        haha2 = mat[z1][z2+1]
        haha3 = mat[z1][z2+2]
        haha4 = mat[z1+1][z2]
        haha5 = mat[z1+1][z2+1]
        haha6 = mat[z1+1][z2+2]
        haha7 = mat[z1+2][z2]
        haha8 = mat[z1+2][z2+1]
        haha9 = mat[z1+2][z2+2]

        bobo = haha1 + haha2 + haha3\
               + haha4 +haha5 + haha6\
               + haha7 + haha8 + haha9

        if bobo > max_sum:
            max_sum = bobo
            mati = [haha1, haha2, haha3], \
                    [haha4, haha5, haha6],\
                    [haha7, haha8, haha9]

# print(x, y)
# print(mat)
print(f"Sum = {max_sum}")
print(*mati[0])
print(*mati[1])
print(*mati[2])

# for z3 in range(3):