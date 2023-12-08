my_list = input().split(', ')

haha = sorted(my_list, key=lambda x: (-len(x),(x)))

# 01. Programming Fundamentals Mid Exam Retake.reverse()

# haha3 = sorted(my_list, key=reversed(my_list))

# print(my_list)
print(haha)
# print(haha3)
# print(haha2)
