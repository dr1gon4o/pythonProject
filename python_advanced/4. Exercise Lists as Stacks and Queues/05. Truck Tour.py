from collections import deque

# pump = int(input())
# info = [int(x, y) for x, y in input().split()]
# info = input().split()

info = deque([[int(x) for x in input().split()] for i in range(int(input()))])
info2 = info.copy()
tank = 0
km = 0

while info2:
    x, y = info2.popleft()

    tank += x

    if tank >= y:
        tank -= y
    else:
        info.rotate(-1)
        info2 = info.copy()
        km += 1
        tank = 0



# print(info)
# print(tank)
print(km)

