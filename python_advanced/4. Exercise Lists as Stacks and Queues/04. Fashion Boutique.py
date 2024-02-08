
box = [int(x) for x in input().split(" ")]
rack = int(input())
rack2 = rack
racken = 1
# summ = 0

while box:
    hoho = box.pop()

    if rack2 >= hoho:
        rack2 -= hoho
    else:
        racken += 1
        rack2 = rack - hoho


# print(box)
# print(summ)
print(racken)
