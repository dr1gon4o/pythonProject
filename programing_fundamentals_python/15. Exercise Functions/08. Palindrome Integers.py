num = input().split(', ')

# numd = [int(x) for x in num]

for i in num:
    if i == i[::-1]:
        print("True")
    else:
        print("False")

# print(num)
# print(numd)
