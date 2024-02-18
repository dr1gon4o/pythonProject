num = int(input())
list = [[int(x) for x in input().split()] for _ in range(num)]

diag = [list[row][row] for row in range(len(list))]
diag2 = [list[row][num - row - 1] for row in range(len(list))]

sumodif = sum(diag) - sum(diag2)

# print(f"Primary diagonal: {', '.join(str(x) for x in diag)}. Sum: {sum(diag)}")
# print(f"Secondary diagonal: {', '.join(str(x) for x in diag2)}. Sum: {sum(diag2)}")
print(abs(sumodif))