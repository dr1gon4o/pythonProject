my_list = input().split(',')

list = list(map(int, my_list))

# list2 = [num for num in list if list[x] % 2 == 0]
# list3 = sorted(list, key=lambda x: x if  )

list2 = []
for x in list:
    if x % 2 == 0:
        list2.append(list.index(x))


# print(my_list)
# print(list)
print(list2)
