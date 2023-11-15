my_list = input().split(' ')
pal = input()

found = 0
for x in my_list:
    if pal == x:
        found += 1

list = [x for x in my_list if x == x[::-1]]


# print(my_list)
print(list)
print(f"Found palindrome {found} times")