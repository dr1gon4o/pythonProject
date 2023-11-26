num = input().split()

numd = [int(x) for x in num]

# def fifi():
#     for x in numd:
#         if abs(x) % 2 != 0:
#             numd.remove(x)
#     return numd
haha = []
for x in numd:
    if abs(x) % 2 == 0:
        haha.append(x)
        # num.remove(x)

# print(num)
# print(numd)
print(haha)
# print(fifi())
# print(filter(fifi(), numd))
