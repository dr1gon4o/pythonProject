message = int(input())

for x in range (0, message):
    numb = int(input())

    if numb == 88:
        print("Hello")
    elif numb == 86:
        print("How are you?")
    elif numb != (88 or 86) and (numb < 88):
        print("GREAT!")
    else:
        print("Bye.")
