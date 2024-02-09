num = int(input())

seto = set()
for _ in range(num):
    line, line2 = [x.split(',') for x in input().split('-')]

    seto1 = set(range(int(line[0]), int(line[1]) + 1))
    seto2 = set(range(int(line2[0]), int(line2[1]) + 1))

    bobo = seto1 & seto2

    if len(bobo) > len(seto):
        seto = bobo


# haha = []
# for x in range(num):
#     line = [x for x in input().split('-')]
#     haha.append(line)

# haha2 = []
# haha3 = []
# for x in haha:
#     bobo = [x for x in x[0].split(",")]
#     bobo2 = [x for x in x[1].split(",")]
#     haha2.append(bobo)
#     haha3.append(bobo2)
#     seto = set(range(int(haha2[0]), int(haha2[1])))
#     print(seto)

# seto = set(range(int(haha2[0], int(haha2[1]))))
# for x in haha2:
#     for y in range(x[0], x[1]):
#         seto.append(x)

# seto2 = set()
# seto3 = set()

# print(seto)

# print(haha)
# print(haha2)
# print(haha3)
print(f"Longest intersection is [{', '.join(str(x) for x in seto)}] with length {len(seto)}")
