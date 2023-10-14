n = int(input())

x1 = []
x2 = []
x3 = 0
x4 = 0

for i in range(n):
    data = int(input())
    if data > 0:
        x1.append(data)
        x3 = len(x1)
    else:
        x2.append(data)
        x4 = sum(x2)

print(f'{x1}\n{x2}\nCount of positives: {x3}\nSum of negatives: {x4}')
