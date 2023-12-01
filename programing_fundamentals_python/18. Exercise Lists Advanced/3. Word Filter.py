list = input().split()

haha = [x for x in list if len(x) % 2 == 0]

for i in haha:
    print(i)

# print(haha.pop(), end=' ')
