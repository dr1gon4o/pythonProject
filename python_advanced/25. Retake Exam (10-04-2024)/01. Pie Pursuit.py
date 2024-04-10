from collections import deque

conts = deque(int(x) for x in input().split(" "))
pies = deque(int(x) for x in input().split(" "))

# while pies or conts:
while True:
    haha = conts.popleft()
    haha2 = pies.pop()

    if haha > haha2:
        haha -= haha2
        if haha > 0:
            conts.append(haha)
    elif haha2 > haha:
        haha2 -= haha

        if haha2 == 1:
            if pies:
                hoho = pies.pop()
                hoho += 1
                pies.append(hoho)
            else:
                pies.append(haha2)
        elif haha2 > 1:
            pies.append(haha2)

    if not conts or not pies:
        break

if conts and not pies:
    # hihi = ', '.join(str(x) for x in conts)
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in conts)}")
elif not conts and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")
else:
    print("We have a champion!")

# if pies and haha > 1:
#     if
#
# else:
#     pies.append(haha2)
# if haha2 > 1:
#     pies.append(haha2)




