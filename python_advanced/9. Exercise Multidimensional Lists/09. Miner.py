# def find(element, matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == element:
#                 return i, j

num = int(input())
command = input().split()
mat = [input().split() for n in range(num)]

coal_number = 0

start = 's'
coal = 'c'
end = 'e'
regular = '*'

row_index = 0
col_index = 0

for ii in enumerate(mat):
    for j in ii[1]:
        if j == start:
            row_index = ii[0]
            col_index = mat[row_index].index(start)


# start_position = find(start,mat)
# row_index = start_position[0]
# col_index = start_position[1]

start_position = mat[row_index][col_index]
# current_position = mat[row_index][col_index]

all_coal = 0
for l in mat:
    for o in l:
        if o == coal:
            all_coal += 1


for i in command:

    if (0 <= row_index < num) and (0 <= col_index < num):
        if i == 'up':
            # current_position = mat[row_index-1][col_index]
            row_index -= 1
        elif i == 'down':
            # current_position = mat[row_index+1][col_index]
            row_index += 1
        elif i == 'left':
            # current_position = mat[row_index][col_index-1]
            col_index -= 1
        elif i == 'right':
            # current_position = mat[row_index-1][col_index+1]
            # row_index, col_index = row_index-1, col_index+1
            col_index += 1
        pass
    else:
        continue

    if row_index < 0:
        row_index = 0
    elif col_index < 0:
        col_index = 0
    elif row_index == num:
        row_index = num-1
    elif col_index == num:
        col_index = num-1
    # if i == 'up':
    #     # current_position = mat[row_index-1][col_index]
    #     row_index -= 1
    # elif i == 'down':
    #     # current_position = mat[row_index+1][col_index]
    #     row_index += 1
    # elif i == 'left':
    #     # current_position = mat[row_index][col_index-1]
    #     col_index -= 1
    # elif i == 'right':
    #     # current_position = mat[row_index-1][col_index+1]
    #     # row_index, col_index = row_index-1, col_index+1
    #     col_index += 1

    current_position = mat[row_index][col_index]
    start_position = current_position

    if current_position == end or coal_number == all_coal:
        break
    if current_position == coal:
        coal_number += 1
        mat[row_index][col_index] = regular


if start_position == end:
    print(f"Game over! ({row_index}, {col_index})")
elif coal_number == all_coal:
    print(f"You collected all coal! ({row_index}, {col_index})")
else:
    print(f"{all_coal - coal_number} pieces of coal left. ({row_index}, {col_index})")

# print(mat)
# print(start_position)
# print(current_position)
# print(f"You collected all coal! ({row_index}, {col_index})")
# print(f"Game over! ({row_index}, {col_index})")
# print(f"{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})")

