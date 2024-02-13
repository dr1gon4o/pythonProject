from collections import deque

choco = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))

milko = 0

while milko != 5 and choco and milk:
    cho = choco.pop()
    mil = milk.popleft()

    if cho <= 0 and mil <= 0:
        continue
    elif cho <= 0:
        milk.appendleft(mil)
        continue
    elif mil <= 0:
        choco.append(cho)
        continue

    if cho == mil:
        milko += 1
    else:
        milk.append(mil)
        choco -= 5
        choco.append(cho)
    # for x in reversed(choco2):
    #     if x <= 0:
    #       choco.remove(x)
    #     if x == milk[0]:
    #         # choco.pop()
    #         # milk.popleft()
    #         milko += 1
    #     else:
    #         milk.append(milk.pop())
    #         choco -= 5
    #         choco.append(x)

# print(milko)
# print(choco)
# print(milk)

if milko == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if choco:
    print(f"Chocolate: {', '.join(str(x) for x in choco)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")
