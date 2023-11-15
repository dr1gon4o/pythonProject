my_list = []
# priority = []
# haha = []
# haha2 = []

while True:
    command = input()
    if command == "End":
        break

    # num = command[0]
    # note = command[1]
    # my_list = command.split('-')
    my_list.append(command)

    priority = sorted(my_list, key=lambda x: int(x.split('-')[0]))
    haha3 = [command.split('-')[1] for command in priority]

    # haha.append(command.split('-')[1])
    # haha2 = sorted(haha, key=lambda x: num)


# print(my_list)
# print(priority)
# print(haha)
print(haha3)

