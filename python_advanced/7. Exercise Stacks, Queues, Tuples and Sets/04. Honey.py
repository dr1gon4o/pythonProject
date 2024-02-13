from collections import deque

bees = deque(int(x) for x in input().split())
nek = [int(x) for x in input().split()]
sym = deque(x for x in input().split())

hiv = 0

while bees and nek:
    be = bees.popleft()
    ne = nek.pop()
    # sim = sym.popleft()

    if ne >= be:
        if sym[0] == "/" and ne == 0:
            pass
            # result = (eval(f"{be} {sym[0]} {ne}"))
            # hiv += abs(result)
            # sym.popleft()
        else:
            result = (eval(f"{be} {sym[0]} {ne}"))
            hiv += abs(result)
            sym.popleft()
        # bees.append(be)
    else:
        # nek.remove(ne)
        bees.appendleft(be)

print(f"Total honey made: {hiv}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
elif nek:
    print(f"Nectar left: {', '.join(str(x) for x in nek)}")
