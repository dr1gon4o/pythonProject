n = int(input())

# popo = False

for i in range(1, 10):
    for j in range(1, 10):
        for l in range(1, 10):
            for d in range(1, 10):
                popo = n % i == 0 and n % j == 0 and n % l == 0 and n % d == 0
                # if n % i == 0:
                #     popo = True
                # if n % j == 0:
                #     popo = True
                # if n % l == 0:
                #     popo = True
                # if n % d == 0:
                #     popo = True
                if popo:
                    print(f'{i}{j}{l}{d}', end=' ')
