line = input()

hoho = {}
all = 0

while line != "Complete":
    haha = line.split()
    k = haha[2]
    v = int(haha[1])

    if haha[0] == "Receive":
        if v <= 0:
            pass
        else:
            if k not in hoho.keys():
                hoho[k] = v
            else:
                hoho[k] += v

    if haha[0] == "Sell":
        if k not in hoho.keys():
            print(f"You do not have any {k}.")
        else:
            if v > hoho[k]:
                all += hoho[k]
                # hoho[k] -= hoho[k]
                print(f"There aren't enough {k}. You sold the last {hoho[k]} of them.")
                hoho.pop(k)
            else:
                all += v
                hoho[k] -= v
                print(f"You sold {v} {k}.")
                if hoho[k] == 0:
                    hoho.pop(k)

    line = input()

for i, u in hoho.items():
    print(f"{i}: {u}")
print(f"All sold: {all} goods")

# print(hoho)
