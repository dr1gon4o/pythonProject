n = int(input())
mat = []

for i in range(n):
    mat.append(list(input()))

elem = input()
is_found = False

for x in range(n):
    if is_found:
        break
    for y in range(len(mat[x])):
        if mat[x][y] == elem:
            print(f"({x}, {y})")
            is_found = True
            break
        #else:
            #print('element is not found')

if not is_found:
    print(f"{elem} does not occur in the matrix")
