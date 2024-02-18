from collections import deque

mon = deque([int(x) for x in input().split(" ")])
# mon = deque(mon2)
fod = deque([int(y) for y in input().split(" ")])
# fod = deque(fod2)

henry = 0

while True:
    haha = mon.pop()
    haha2 = fod.popleft()
    # hehe = fod.

    if haha == haha2:
        henry += 1
        # continue
    elif haha > haha2:
        henry += 1
        hoho = haha - haha2
        # mon[::-1] += hoho
        if mon:
            hoho2 = mon.pop()
            hoho3 = hoho2 + hoho
            mon.append(hoho3)
        else:
            # hoho4 = haha + hoho
            mon.append(hoho)
        # continue
    else:
        pass

    if not mon or not fod:
        break

if henry >= 4:
    print(f"Gluttony of the day! Henry ate {henry} foods.")
elif 0 < henry < 4:
    # print(f"Henry ate: {henry} foods.")
    if henry == 1:
        print(f"Henry ate: {henry} food.")
    else:
        print(f"Henry ate: {henry} foods.")
# elif henry == 1:
#     print(f"Henry ate: {henry} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
