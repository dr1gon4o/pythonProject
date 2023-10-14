command = input()

coffee = 0

while True:

    if command == 'END':
        break

    if command.islower():
        if command.lower() == 'coding' \
                or command.lower() == 'dog' \
                or command.lower() == 'cat' \
                or command.lower() == 'movie':
            coffee += 1
        else:
            pass
    elif command.isupper():
        if command.lower() == 'coding' \
                or command.lower() == 'dog' \
                or command.lower() == 'cat' \
                or command.lower() == 'movie':
            coffee += 2
        else:
            pass

    command = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
