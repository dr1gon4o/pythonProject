def concatenate(*haha, **haha2):
    list = "".join(haha)

    for x,y in haha2.items():
        if x in list:
            list = list.replace(x, y)

    return list

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
