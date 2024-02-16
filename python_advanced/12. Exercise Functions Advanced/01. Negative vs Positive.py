sumne = []
sumpo = []
# abne = sum(sumne)
# abpo = sum(sumpo)

num = [int(x) for x in input().split()]

for x in num:
    u = int(x)
    if u > 0:
        sumpo.append(u)
    else:
        sumne.append(u)
# while num:
#
#     for x in num:
#         u = int(x)
#         if u > 0:
#             sumpo.append(u)
#         else:
#             sumne.append(u)
#     break

abne = sum(sumne)
abpo = sum(sumpo)

print(abne)
print(abpo)
if abs(abne) > abpo:
    print("The negatives are stronger than the positives")
elif abpo > abs(abne):
    print("The positives are stronger than the negatives")
