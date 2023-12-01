# list = input().split(', ')

# list2 = [int(x) for x in list]
list2 = [int(x) for x in input().split(', ')]

# haha = sorted(list2)
# list3 = []
# list4 = []
gr = 10

# for x in list2:
#     if x <= gr:
#         list3.append(x)
#     print(f"Group of {gr}'s: {list3}")
#     gr += 10
#     if x not in list3:
#         list4.append(x)

while list2:
    list3 = [x for x in list2 if x <= gr]
    print(f"Group of {gr}'s: {list3}")
    gr += 10
    list2 = [x for x in list2 if x not in list3]

# print(list)
# print(list2)
# print(list3)
# print(list4)
# print(haha)
# print(sorted(list2))
# print(max(list))
# print(max(list2))

# print(f"Group of {group}'s: {list_of_numbers}")

