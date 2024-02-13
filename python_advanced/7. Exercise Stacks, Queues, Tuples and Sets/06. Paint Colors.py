from collections import deque

line = deque(input().split())

list = {"red", "yellow", "green", "blue", "orange", "purple"}
req_list = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"}
}

dodo = []
# list2 = {"orange": "red + yellow", "purple": "red + blue", "green": "yellow + blue"}

while line:
    haha = line.popleft()
    haha2 = line.pop() if line else ""
    # haha3 = f"{haha} + {haha2}"

    # for x,y in list2.items():
    #     if haha3 == x:
    #         list.append(y)
    #     else:
    #         pass
    for color in (haha + haha2, haha2 + haha):
        if color in list:
            dodo.append(color)
            break
    else:
        for element in (haha[:-1], haha2[:-1]):
            if element:
                line.insert(len(line) // 2, element)

for color in set(req_list.keys()).intersection(dodo):
    if not req_list[color].issubset(dodo):
        dodo.remove(color)

print(dodo)







# colors = {"red", "yellow", "green", "blue", "orange", "purple"}
# req_colors = {
#     "orange": {"red", "yellow"},
#     "purple": {"blue", "red"},
#     "green": {"yellow", "blue"}
# }


