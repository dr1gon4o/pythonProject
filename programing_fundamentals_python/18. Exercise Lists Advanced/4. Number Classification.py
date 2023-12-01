list = input().split(', ')

haha = [int(x) for x in list]

po = []
ne = []
ev = []
od = []

for i in haha:
    if i >= 0:
        po.append(i)
    if i < 0:
        ne.append(i)
    if i % 2 == 0:
        ev.append(i)
    if i % 2 != 0:
        od.append(i)

print(f"Positive: {', '.join(map(str, po))}")
print(f"Negative: {', '.join(map(str, ne))}")
print(f"Even: {', '.join(map(str, ev))}")
print(f"Odd: {', '.join(map(str, od))}")


# vtori variant p burz moi: sled tova printovete
# po = [int(x) for x in list if x >= 0]
# ne = [int(x) for x in list if x < 0]
# ev = [int(x) for x in list if x % 2 == 0]
# od = [int(x) for x in list if x % 2 != 0]

# print(list)
# print(haha)
# print(f"Negative: {po}")
# print(f"Negative: {ne}")
# print(f"Even: {ev}")
# print(f"Odd: {od}")
