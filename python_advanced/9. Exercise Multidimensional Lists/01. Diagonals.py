num = int(input())
list = [[int(x) for x in input().split(", ")] for _ in range(num)]

diag = [list[row][row] for row in range(len(list))]
diag2 = [list[row][num - row - 1] for row in range(len(list))]

# hoho = list[0]
# hoho2 = list[1][1]
# hoho3 = list[2][2]
# hoho4 = list[0][2]
# hoho5 = list[1][1]
# hoho6 = list[2][0]

# sum = list[0] + list[1][1] + list[2][2]
# sumo = hoho + hoho2 + hoho3
# sum2 = list[0][2] + list[1][1] + list[2][0]
# sumo2 = list[0][2] + list[1][1] + list[2][0]

# print(list)
# print(list2)
# print(type(list))
# print(sumo)
# print(sumo2)
print(f"Primary diagonal: {', '.join(str(x) for x in diag)}. Sum: {sum(diag)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in diag2)}. Sum: {sum(diag2)}")
# print(diag)
# print(diag2)
