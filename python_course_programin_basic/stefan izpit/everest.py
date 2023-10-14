x = input()
# meters = int(input())


x2 = 5364
x3 = 1

while True:
    # if x == 'END':
    #     break

    meters = int(input())
    # x3 += 1
    if x == 'Yes':
        x3 += 1
        x2 = x2 + meters
    if x == 'No':
        x2 = x2 + meters
    if x2 >= 8848:
        break

    if x3 == 5:
        break
    if x == 'END':
        break
    x = input()

if x2 >= 8848:
    print(f"Goal reached for {x3} days!")
else:
    print("Failed!")
    print(x2)