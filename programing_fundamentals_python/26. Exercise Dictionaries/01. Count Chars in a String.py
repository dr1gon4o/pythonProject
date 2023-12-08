diki = input().split()

# 01. Programming Fundamentals Mid Exam Retake = {x for x in diki}
haha2 = []
haha3 = {}

for x in diki:
    for i in x:
        haha2.append(i)
#         print(f"{i} -> {len(i)}")

for k in haha2:
    if k not in haha3.keys():
        haha3[k] = 0
    haha3[k] += 1
    # else:
    #     haha3[k] = 0
for f, g in haha3.items():
    print(f"{f} -> {g}")



# print(diki)
# print(01. Programming Fundamentals Mid Exam Retake)
# print(haha2)
# print(haha3)

