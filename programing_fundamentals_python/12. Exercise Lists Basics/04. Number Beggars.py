string = input().split(', ')
beggars = int(input())

my_list = []
for number in string:
    my_list.append(int(number))

final_sum = []
start_index = 0

while start_index < beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(my_list), beggars):
        current_beggar_sum += my_list[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1
print(final_sum)
