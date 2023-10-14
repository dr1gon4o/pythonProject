begin_num = input()
end_num = input()

for i in range(int(begin_num[0]), int(end_num[0]) + 1):
    for j in range(int(begin_num[1]), int(end_num[1]) + 1):
        for k in range(int(begin_num[2]), int(end_num[2]) + 1):
            for m in range(int(begin_num[3]), int(end_num[3]) + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and m % 2 != 0:
                    print(f"{i}{j}{k}{m}", end=" ")