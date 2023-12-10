line = input().split()
# haha, haha2 = input().split()

# sum = 0
# sum2 = 0
total = 0

haha = line[0]
haha2 = line[1]

if len(haha) > len(haha2):
    for x in range(len(haha2)):
        total += ord(haha[x]) * ord(haha2[x])
    for x in range(len(haha2), len(haha)):
        total += ord(haha[x])

elif len(haha) < len(haha2):
    for x in range(len(haha)):
        total += ord(haha[x]) * ord(haha2[x])
    for x in range(len(haha), len(haha2)):
        total += ord(haha2[x])

elif len(haha) == len(haha2):
    for x in range(len(haha)):
        total += ord(haha[x]) * ord(haha2[x])

print(total)
# print(haha)
# print(haha2)

