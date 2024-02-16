def even_odd(*haha):
    # haha2 = list(haha)
    # haha3 = [int(x) for x in haha if not "even" or " odd"]
    hoho = haha[-1]

    if hoho == "even":
        return [x for x in haha[:-1] if x % 2 == 0]
    else:
        return [x for x in haha[:-1] if x % 2 != 0]

    # return haha2

print(even_odd(1, 2, 3, 4, 5, 6, "even"))