list = input().split()
count = int(input())

haha = []
for i in list:
    haha.append(int(i))

for k in range(count):
    haha.remove(min(haha))

haha2 = ', '.join(str(x) for x in haha)

# list.sort()
# list.remove(min(list))
# list.remove(min(list))

# print(haha)
print(haha2)
# print(list)
# print(list.sort())
# print(haha)
# # print(haha2)
# print(', '.join(haha))


# for i in range(-1, count):
#     list_string.remove(min(list_string))

# haha = int(list)
# for k in list:
#     haha = list.remove(min(list))

# for i in range(count):
#     list.remove(min(list))