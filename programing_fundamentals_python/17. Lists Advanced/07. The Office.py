my_list = input().split(' ')

fact = int(input())

list1 = list(map(int, my_list))
list2 = list(map(lambda x: x * fact, list1))

# list3 = list(map(lambda x: x * fact, my_list))
# list4 = []

# for x in my_list:
#     list4.append(x * fact)
def average(list2):
    avg = sum(list2) / len(list2)
    return avg


happy = 0
for x in list2:
    if x > average(list2):
        happy += 1


if happy >= average(list2):
    print(f"Score: {happy}/{len(list2)}. Employees are happy!")
else:
    print(f"Score: {happy}/{len(list2)}. Employees are not happy!")

# print(my_list)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
