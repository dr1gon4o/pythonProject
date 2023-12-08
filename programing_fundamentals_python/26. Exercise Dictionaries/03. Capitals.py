cont = input().split(", ")
citi = input().split(", ")

haha = list(zip(cont, citi))

haha2 = {k: x for (k, x) in haha}

for k, x in haha2.items():
    print(f"{k} -> {x}")

# print(cont)
# print(citi)
# print(haha)
# print(haha2)
