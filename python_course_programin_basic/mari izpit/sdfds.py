K = int(input())
L = int(input())
M = int(input())
N = int(input())

popo = False

for i in range(K, 8 + 1):
    for l in range(L, 9 + 1):
        for j in range(M, 8 + 1):
            for p in range(N, 9 + 1):
                if i % 2 != 0:
                    break
                # if l % 2 == 0:
                #     break
                if j % 2 != 0:
                    break
                # if p % 2 == 0:
                #     break
                if f"{i}{l}" == f"{j}{p}":
                    print("Cannot change the same player.")
                else:
                    print(f"{i}{l} - {j}{p}")
