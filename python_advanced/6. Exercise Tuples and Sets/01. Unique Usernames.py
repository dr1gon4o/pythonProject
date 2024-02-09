num = int(input())

seto = set()

for x in range(num):
    name = input()
    seto.add(name)

print(*seto, sep='\n')

