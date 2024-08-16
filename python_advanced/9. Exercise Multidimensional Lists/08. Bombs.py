num = int(input())
# mat = [map(int, input().split()) for x in range(num)]
mat = [[int(el) for el in (input().split())] for el in range(num)]

command = [el.split(",") for el in input().split()]

alive_cells = 0
sum_cells = 0

for x in command:
    haha = int(x[0])
    haha2 = int(x[1])
    bomb = mat[haha][haha2]
    # print(bomb)
    for y in mat:
        pp = mat.index(y)

        if pp == haha or pp == haha +1 or pp == haha-1:

            for o in enumerate(y):
                hoho = o[1] - bomb
                i = o[0]
                if i == haha2 or i == haha2 +1 or i == haha2 -1:
                    if o[1] <= 0:
                        continue
                    else:
                        y[i] = hoho

for x in mat:
    for y in x:
        if y > 0:
            alive_cells += 1
            sum_cells += y

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_cells}")
# print(mat)
[print(*el) for el in mat]
# print(command)

