string = ""
line = input()

while line != "End":
    haha = line.split()

    if haha[0] == "Add":
        string += haha[1]
    elif haha[0] == "Upgrade":
        # po = ord(haha[1]) +1
        # do = chr(po)
        # string.replace(haha[1], do)
        for x in string:
            if haha[1] == x:
                po = ord(x)
                do = chr(po +1)
                string = string.replace(x, do)
    elif haha[0] == "Print":
        print(string)
    elif haha[0] == "Index":
        if haha[1] in string:
            go = []
            for x in range(len(string)):
                if string[x] == haha[1]:
                    go.append(x)
            # for char in string:
            #     if haha[1] == char:
            #         go.append(string.index(char))
            print(*go, sep=" ")
        else:
            print("None")
    elif haha[0] == "Remove":
        while haha[1] in string:
            string = string.replace(haha[1], "")

        # string = string.remove
        # if haha[1] in string:
        #     string.replace(haha[1], "")
        # for x in string:
        #     if haha[0] == x:
        #         for u in string:
        #             string = string.replace(u, "")

    line = input()

# print(string)
