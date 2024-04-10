def draw_cards(*haha, **haha2):
    monsters = []
    spells = []

    for x, y in haha:
        if y == "monster":
            if x not in monsters:
                monsters.append(x)
        elif y == "spell":
            if x not in spells:
                spells.append(x)

    for z, v in haha2.items():
        if v == "monster":
            if z not in monsters:
                monsters.append(z)
        if v == "spell":
            if z not in spells:
                spells.append(z)

    monsters.sort(reverse=True)
    spells.sort()

    result = []
    if monsters:
        result.append("Monster cards:")
        for card in monsters:
            result.append(f"  ***{card}")
    if spells:
        result.append("Spell cards:")
        for card in spells:
            result.append(f"  $$$${card}")

    return "\n".join(result)

    # result = ""
    # if monsters:
    #     result.append("Monster cards:")
    #     for card in monsters:
    #         result.append(f"  ***{card}")
    # if spells:
    #     result.append("Spell cards:")
    #     for card in spells:
    #         result.append(f"  $$$${card}")
    #
    # return "\n".join(result


# print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))

# print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
# result = ""
# if monsters and spells:
#     print("Monster cards:")
#     for x in monsters:
#         print(f"  ***{x}")
#     print("spells cards:")
#     for y in spells:
#         print(f"  $$${y}")
# elif monsters:
#     print("Monster cards:")
#     for x in monsters:
#         print(f"  ***{x}")
# elif spells:
#     print("spells cards:")
#     for y in spells:
#         print(f"  $$${y}")
# return