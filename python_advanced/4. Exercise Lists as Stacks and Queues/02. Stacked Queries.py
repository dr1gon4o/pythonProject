num = int(input())

haha = []

for i in range(num):
    hoho = [int(x) for x in input().split(" ")]
    if hoho[0] == 1:
        haha.append(hoho[1])
    elif hoho[0] == 2:
        if haha:
            haha.pop()
    elif hoho[0] == 3:
        if haha:
            print(max(haha))
    elif hoho[0] == 4:
        if haha:
            print(min(haha))

haha.reverse()
haha2 = map(str, haha)
print(", ".join(haha2))
