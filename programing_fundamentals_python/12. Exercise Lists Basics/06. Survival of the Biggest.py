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

# print(01. Programming Fundamentals Mid Exam Retake)
print(haha2)
# print(list)
# print(list.sort())
# print(01. Programming Fundamentals Mid Exam Retake)
# # print(haha2)
# print(', '.join(01. Programming Fundamentals Mid Exam Retake))


# for i in range(-1, count):
#     list_string.remove(min(list_string))

# 01. Programming Fundamentals Mid Exam Retake = int(list)
# for k in list:
#     01. Programming Fundamentals Mid Exam Retake = list.remove(min(list))

# for i in range(count):
#     list.remove(min(list))