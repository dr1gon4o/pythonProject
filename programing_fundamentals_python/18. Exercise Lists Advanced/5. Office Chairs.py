num = int(input())

# haha = []
hoho = 0
alert = 0

for i in range(1, num +1):
    list = input().split()
    # print(list)

    # if len(list[0]) > int(list[1]):
    #     hoho += len(list[0]) - int(list[1])
    if len(list[0]) < int(list[1]):
        dodo = int(list[1]) - len(list[0])
        print(f"{dodo} more chairs needed in room {i}")
    else:
        hoho += len(list[0]) - int(list[1])
        alert += 1



    # haha.append(list)

# print(haha)
if alert == num:
    print(f"Game On, {hoho} free chairs left")
