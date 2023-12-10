line = input().split("\\")

# haha = 0
# haha2 = 1

hoho = ""
for x in line:
      if "." in x:
            hoho = x

u = hoho.find(".")
u2 = hoho[u+1:]
u3 = hoho[:u]

# u = line.find(".")
# u3 = 0
# u2 = line[u+1:]
# u4 = line[u3+1:]
# sum = 0
# ha = 0
#
# for x in line:
#       if x == "\\":
#             sum += 1
#             if sum == 3:
#                   u3 = line.find(x)
            #       ha = line[x]
            # print('1')
            # u = line[x[index]

# print(u)
# print(hoho)
# print(u2)
# print(u3)
# print(u4)
# print(ha)
print(f"File name: {u3}\n"
      f"File extension: {u2}")
