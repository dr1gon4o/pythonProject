my_list = input().split(', ')
my_list2 = input().split(', ')

# my_list3 = my_list + my_list2

# my_list4 = list(filter(lambda x: x in my_list, my_list3))
#
# my_list5 = my_list3.copy()

# list33 = [x for x in my_list if x in my_list2]

my_list6 = []
for x in my_list:
    for y in my_list2:
        if x in y and x not in my_list6:
            my_list6.append(x)

# my_list7 = list(set(my_list6))

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)
# print(my_list5)
print(my_list6)
# print(my_list7)
# print(list33)

