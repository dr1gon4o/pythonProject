num = int(input())

list = []
nunu = num

list2 = [(i**2) * 2 for i in range(1, num+1)]

list3 = []
for x in list2:
    if nunu == 0:
        break
    if x <= nunu:
        list3.append(x)
        nunu -= x
    else:
        list3.append(nunu)
        nunu -= nunu



# for i in range(1, nunu + 1):
#     # list.append(i)
#     if nunu == 0:
#         break
#     haha = (i**2) * 2
#     if haha <= nunu:
#         list.append(haha)
#         nunu -= haha

# print(list)
# print(list2)
print(list3)
