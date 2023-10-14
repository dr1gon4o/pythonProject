n = int(input())
x = input()
lists = []

for i in range(n):
    x2 = input()
    lists.append(x2)
print(lists)

for i in range(len(lists) -1, -1, -1):
    x3 = lists[i]
    if x not in x3:
        lists.remove(x3)
print(lists)
