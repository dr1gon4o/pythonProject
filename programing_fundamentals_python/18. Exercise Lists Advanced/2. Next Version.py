# my_list = input().split('.')
#
# my_list2 = list(map(int, my_list))

my_list2 = [int(haha) for haha in input().split('.')]
my_list2[-1] += 1

# my_list3 = [my_list2[-1] +1]

# my_list4 = []
# for x in my_list2:
#
#     my_list4.append(x)
#     # my_list4[-1] += 1
#     if x == my_list2[-1]:
#         my_list4[-1] += 1
#     if x == 9:
#         # x = 0
#         my_list4[-1] = 0
#         my_list4[-2] += 1

for x in range(len(my_list2) -1, -1, -1):
    if my_list2[x] > 9:
        my_list2[x] = 0
        if x - 1 >= 0:
            my_list2[x -1] += 1

my_list3 = list(map(str, my_list2))
my_list5 = '.'.join(my_list3)

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)
print(my_list5)
