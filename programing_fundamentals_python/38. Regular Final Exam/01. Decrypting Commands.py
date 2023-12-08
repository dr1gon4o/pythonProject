command1 = input()
command2 = input().split(' ')


while True:
    if command2 == "Finish":
        break

    if command2[0] == 'Replace':
        command1 = command1.replace(command2[1], command2[2])
        print(command1)

    if command2[0] == 'Make':
        if command2[1] == 'Upper':
            haha = command1.upper()
            print(haha)
        if command2[1] == 'Lower':
            haha = command1.lower()
            print(haha)
    if command2[0] == 'Check':
        if command2[1] in haha:
            print(f'Message contains {command2[1]}')
        else:
            print(f"Message doesn't contain {command2[1]}")
    if command2[0] == 'Sum':
        start = command2[1]
        ennd = command2[2]
        dodo = haha[int(start):int(ennd)+1]
        hoho2 = 0
        for x in dodo:
            hoho2 += ord(x)
        if hoho2 == 0:
            print("Invalid indices!")
        else:
            print(hoho2)


    if command2[0] == 'Cut':
        start = command2[1]
        ennd = command2[2]
        dodo = haha[int(start):int(ennd) +1]
        dodo2 = haha.replace(dodo, '')
        # if int(start) < len(01. Programming Fundamentals Mid Exam Retake):
        #     print("Invalid indices!")
        if len(haha) < int(ennd):
            print("Invalid indices!")
        elif int(start) <= 0 :
            print("Invalid indices!")
        else:
            print(dodo2)



        # print(dodo2)

    command2 = input().split(' ')

