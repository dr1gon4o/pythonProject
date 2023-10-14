numb = int(input())


for x in range(numb):
    string = input()

    if '_' in string or ',' in string or '.' in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
