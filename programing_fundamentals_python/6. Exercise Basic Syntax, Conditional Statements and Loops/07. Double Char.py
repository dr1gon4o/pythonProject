command = input()

while True:

    if command == 'End':
        break
    if command == "SoftUni":
        command = input()
        continue

    text = ''
    for char in command:
        text += char * 2
    print(text)

    command = input()
