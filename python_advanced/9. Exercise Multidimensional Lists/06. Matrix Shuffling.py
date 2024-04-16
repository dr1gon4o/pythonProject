
x, y = [int(el) for el in input().split()]

# mat = []
#
# for i in range(x):
#     mat.append([int(el) for el in (input().split())])

# tova e sukratenoto
mat = [[el for el in (input().split())] for el in range(x)]

command = input().split()

while command[0] != 'END':

    if command[0] != "swap":
        print(f"Invalid input!")
        command = input().split()
        continue
    elif len(command) != 5:
        print(f"Invalid input!")
        command = input().split()
        continue
    # if command == "END":
    #     break

    haha1 = int(command[1])
    haha2 = int(command[2])
    haha3 = int(command[3])
    haha4 = int(command[4])

    if haha1 not in range(x) and haha3 not in range(x):
        print(f"Invalid input!")
        command = input().split()
        continue
    elif haha2 not in range(y) and haha4 not in range(y):
        print(f"Invalid input!")
        command = input().split()
        continue


    hoho1 = mat[haha1][haha2]
    hoho2 = mat[haha3][haha4]

    mat[haha1][haha2] = hoho2
    mat[haha3][haha4] = hoho1
    # print(*mat,sep='\n')
    [print(*el) for el in mat]

    # if command == "END":
    #     break

    command = input().split()

# print(x, y)
# print(mat)
# print(*mat)
# print(*mat,sep='\n')
# print(command)
# [print(*el) for el in mat]

# tova e sushtoto kato tova [print(*el) for el in mat]!
# for el in mat:
#     print(*el)



# drugo reshenie s funkcii (mai e po lesno)!
# def check_indices_valid(indices):  # row1=1 col1=2 row2=0 col2=2
#     return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)
#
# def swap_elements(command, indices):
#     if len(indices) == 4 and check_indices_valid(indices) and command == "swap":
#         row1, col1, row2, col2 = indices  # [2, 5, 3, 4]
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#
#         [print(*row) for row in matrix]  # row => [1, 2, 3, 4] =>
#     else:
#         print("Invalid input!")
#
#
# rows, cols = [int(x) for x in input().split()]  # row = 3, col = 4
# matrix = [input().split() for _ in range(rows)]
#
# valid_rows = range(rows)  # [0, 1, 2]
# valid_cols = range(cols)  # [0, 1, 2, 3]
#
# while True:
#     command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]  # ["swap", 2, 3, 5, 4]
#
#     if command_type == "END":
#         break
#
#     swap_elements(command_type, coordinates)