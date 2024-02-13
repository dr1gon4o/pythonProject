from collections import deque

box = deque(int(x) for x in input().split())
mag = deque(int(x) for x in input().split())

list = []
# flag = False

while box and mag:

    bo = box.pop() if mag[0] or not box[0] else 0
    ma = mag.popleft() if bo or not mag[0] else 0
    popo = bo * ma

    if popo == 150:
        list.append('Doll')
    elif popo == 250:
        list.append('Wooden train')
    elif popo == 300:
        list.append('Teddy bear')
    elif popo == 400:
        list.append('Bicycle')
    else:
        if popo < 0:
            haha = bo + ma
            box.append(haha)
        elif popo > 0:
            haha2 = bo + 15
            box.append(haha2)

    # if 'Doll' in list and 'Wooden train' in list:
    #     # flag = True
    #     flag += 1
    #     # break
    # elif 'Teddy bear' in list and 'Bicycle' in list:
    #     flag = True
    #     flag += 1
    #     # break

# if flag:
if {'Doll', 'Wooden train'}.issubset(list) or {'Teddy bear', 'Bicycle'}.issubset(list):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if box:
    print(f"Materials left: {', '.join([str(x) for x in box][::-1])}")
elif mag:
    print(f"Magic left: {', '.join(str(x) for x in mag)}")

# haha3 = tuple(list)

# haha3 = {}
# for i in list:
#     if i not in haha3:
#         haha3[i] = 0
#     haha3[i] += 1

# [print(f"{x}: {haha3.count(x)}") for x in haha3]
# [print(f"{x}: {list.count(x)}") for x in list]
# [print(f"{x}: {y}") for x, y in sorted(haha3.items())]
[print(f"{x}: {list.count(x)}") for x in sorted(set(list))]

