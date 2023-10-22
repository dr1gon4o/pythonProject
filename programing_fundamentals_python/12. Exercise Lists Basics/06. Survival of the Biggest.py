list_string = input().split()
count = int(input())

# list_string = list_string.copy()

for i in range(-1, count):

    list_string.remove(min(list_string))

print(list_string)