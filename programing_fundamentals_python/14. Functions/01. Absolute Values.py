list = input().split()

my_list = []

for x in list:
    number = float(x)
    my_list.append(number)

abs_list = [abs(n) for n in my_list]

print(abs_list)
