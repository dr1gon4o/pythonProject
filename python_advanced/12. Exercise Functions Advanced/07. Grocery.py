def grocery_store(**haha):
    cheeses_dict = sorted(haha.items(), key=lambda x: (-x[1],-len(x[0]), x[0]))
    result = []
    for x, y in cheeses_dict:
        result.append(f"{x}: {y}")
    return "\n".join(result)


# -x[1] ще сортира от по-голямот, към по-малкото число в тюпъла,
    # след това сортираме с -len(x[0], за да сортира ключа по дължина - от по-дълга към по-къса
    # и накрая x[0], за да се сортира по азбучен ред

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
