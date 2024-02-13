
seto = set(int(x) for x in input().split())
seto2 = set(int(x) for x in input().split())

for _ in range(int(input())):
    # line, line2 = [x.split(' ') for x in input().split(' ')]
    line = [x for x in input().split(' ')]
    setto = set()
    for x in line:
        if x.isnumeric():
            setto.add(int(x))

    if line[0] == 'Add':
        if line[1] == 'First':
            # [seto.add(int(x)) for x in setto]
            seto = seto | setto
            # seto.update(setto)
        elif line[1] == 'Second':
            # [seto2.add(int(x)) for x in setto]
            seto2 = seto2 | setto
            # seto2.update(setto)
    elif line[0] == 'Remove':
        if line[1] == 'First':
            # [seto.discard(int(x)) for x in setto]
            seto -= setto & seto
            # if setto < seto:
            #     seto.remove(setto)
        elif line[1] == 'Second':
            # [seto2.discard(int(x)) for x in setto]
            seto2 -= setto & seto2
            # if setto in seto2:
            #     seto2.remove(setto)
    elif line[0] == 'Check':
        if seto < seto2 or seto2 < seto:
            print('True')
        else:
            print('False')

print(*sorted(seto), sep=', ')
print(*sorted(seto2), sep=', ')
# print(line)


# tezi listove pod vseki if e ot lekciata stavat.. prosto iskax moia variant.. moje taka i taka da se napishe