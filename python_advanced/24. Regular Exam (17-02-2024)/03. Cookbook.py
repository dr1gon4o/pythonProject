import operator
def cookbook(*haha):
    list = {}

    for x, y, z in haha:
        if y not in list:
            list[y] = {}
        list[y][x] = z

    list = dict(sorted(list.items(), key = lambda x : -len(x[1])))
    # list = dict(sorted(list.values(), key=operator.itemgetter(1)))

    # for x in list.keys():
    #     x = dict(sorted(list.items(), key = lambda x : x[1]))

    for x, y in list.items():
        print(f"{x} cuisine contains {len(list[x])} recipes:")
        for i, z in y.items():
            print(f"  * {i} -> Ingredients: {z[0]}, {z[1]}")
    exit()


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Ratatouil--le", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Ratatouile", "French", ["eggplant", "zucchini", "tomatoes"])
))
