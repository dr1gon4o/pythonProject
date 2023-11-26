haha = []

for x in range(3):
    num = input()
    haha.append(int(num))

haha.sort(reverse=True)

# for i in haha:
#     haha.pop(min(haha))

# haha2 = [haha.pop(min(int(x))) for x in haha]
# print(haha)
# print(haha2)
print(haha.pop())