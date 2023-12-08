# a = {'01. Programming Fundamentals Mid Exam Retake': 2}
# b = a > 2
# if not a:
#     print(a)
# if b:
#     print(b)
# example = None
# for x in a:
#     if example == None:
#         print(x*2)
#     if example is not None:
#         print(x)
#     # if example = None:
#     #     print(x)

# print(bool(0))
# print(bool(None))
# print(bool(""))
# print(bool(-1))

# # x = lambda a: a**3
# # print(x(2))
# for i in range(10, 3, -2):
#     print(i, end=" ")
# def printText(text):
#     print("I love" + text)
# printText("python")

haha = "ILikeSoftUni"
start = 1
ennd = 4
hoho = [x for x in haha]

hoho2 = []
for x in hoho:

    if start <= x <= ennd:
        hoho2.append(x)


print(haha)
print(hoho)
print(hoho2)
