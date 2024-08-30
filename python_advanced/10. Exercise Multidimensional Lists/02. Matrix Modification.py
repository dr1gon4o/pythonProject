num = int(input())
# mat = [input().split() for i in range(num)]
mat = []
for x in range(num):
    hoho = input().split()
    lolo = []
    for y in hoho:
        lolo.append(int(y))
    mat.append(lolo)

# tova e sukratenia variant na tezi for cikli ot gore
# matrix = [[int(n) for n in input().split()] for row in range(num)]

command = input().split()

while True:

    if command[0] == "END":
        break

    haha1 = command[0]
    haha2 = int(command[1])
    haha3 = int(command[2])
    haha4 = int(command[3])

    if haha1 == "Add":
        if haha2 in range(0, len(mat)) and haha3 in range(0, len(mat)):
            mat[haha2][haha3] += haha4
        else:
            print("Invalid coordinates")
            pass
    elif haha1 == "Subtract":
        if haha2 in range(0, len(mat)) and haha3 in range(0, len(mat)):
            mat[haha2][haha3] -= haha4
        else:
            print("Invalid coordinates")
            pass
    command = input().split()
    # if haha1 == "END":
    #     break

[print(*el) for el in mat]
