mat = [i for i in input().split("|")]
mat2 = [i.split(" ") for i in mat]

for x in mat2:
    for y in x:
        if y == '':
            x.remove(y)
for x2 in mat2:
    for y in x2:
        if y == '':
            x2.remove(y)

for t in mat2.__reversed__():
    print(*t, end=" ")

# print(mat)
# [print (*t) for t in mat2.__reversed__()]