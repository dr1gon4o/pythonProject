# x = {0: x for x in [1,2,3]}
# print(x)
a= [[1,2,3],[4,5,6],[7,8,9]]
print(a[1][0])
flat_list = [x for row in a for x in row]
print(flat_list)