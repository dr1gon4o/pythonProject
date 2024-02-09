
haha2 = set()
haha3 = set()
raw = 0
for x in range(int(input())):
    names = input()
    # haha2 = set()
    haha = 0
    raw += 1
    for i in names:
       bobo = ord(i)
       # haha = 0
       haha += bobo
    haha = int(haha/raw)
    if haha % 2 == 0:
        haha2.add(haha)
    else:
        haha3.add(haha)

# print(haha)
if sum(haha3) == sum(haha2):
    print(*haha3|haha2, sep=', ')
elif sum(haha3) > sum(haha2):
    print(*haha3 - haha2, sep=', ')
elif sum(haha3) < sum(haha2):
    print(*haha3 ^ haha2, sep=', ')
