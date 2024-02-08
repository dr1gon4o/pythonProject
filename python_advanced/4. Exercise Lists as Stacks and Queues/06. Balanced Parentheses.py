from collections import deque

line = deque()
line2 = input()
for x in line2:
    line.append(x)

bobo = 0
# print(line)
# print(line2)

while line:
    haha2 = line.pop()
    haha = line.popleft()
    # if haha + haha2 == '{}':
    #     pass
    # elif haha + haha2 == '()':
    #     pass
    # elif haha + haha2 == '[]':
    #     pass
    # else:
    #     bobo += 1
    if f"{haha + haha2}" not in "{}()[]":
        print("NO")
        break
else:
    print('YES')

# if bobo == 0:
#     print('YES')
# else:
#     print('NO')
