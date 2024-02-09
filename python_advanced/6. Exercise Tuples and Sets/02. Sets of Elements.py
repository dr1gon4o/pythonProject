x, y = input().split(" ")

xx = []
xx2 = []

for i in range(int(x)):
    haha = int(input())
    xx.append(haha)

for i in range(int(y)):
    haha2 = int(input())
    xx2.append(haha2)

seto = set(xx)
seto2 = set(xx2)
hoho = seto & seto2

# print(x, y)
# print(seto)
# print(seto2)
# print(seto & seto2)
print(*hoho, sep='\n')
