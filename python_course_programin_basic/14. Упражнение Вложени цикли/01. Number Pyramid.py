n = int(input())

cu = 1
popo = False

for x in range(1, n + 1):
    for x2 in range(1, x + 1):
        if cu > n:
            popo = True
            break
        print(cu,  end=' ')
        cu += 1
    if popo:
        break
    print()


        # print(str(x) + str(x2) + " ", end=' ')
        # print()

