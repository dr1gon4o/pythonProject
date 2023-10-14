x = int(input())
x2 = int(input())
x3 = int(input())

combi = 0
no_combi = False

for i in range(x, x2+1):
    for o in range(x, x2+1):
        combi += 1
        if i + o == x3:
            print(f"Combination N:{combi} ({i} + {o} = {x3})")
            no_combi = True
            break
    if no_combi:
        break
else:
    print(f"{combi} combinations - neither equals {x3}")
