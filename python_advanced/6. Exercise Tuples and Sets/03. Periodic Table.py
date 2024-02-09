num = int(input())

seto = set()

for x in range(num):
    name = input().split(" ")
    for i in name:
        seto.add(i)

print(*seto, sep='\n')
