num = int(input())
state = [int(x) for x in input().split(" ")]

w1 = 0
list = []
nam = num

for i in state:
    don = 4 - i
    # i += don
    if nam > don:
        i += don
        nam -= don
        list.append(i)
    if nam < don:
        list.append(nam)
        nam -= nam
        break

    # if i == 0:
    #     nam -= 4
    #     list.append(i)
    # if i > 0:
    # don = 4 - i
    # i += don
    # nam -= don
    # list.append(i)
    # if nam > don:
    #     nam -= don
    #     i += don
    #     list.append(i)
    # if nam < don:
    #     list.append(nam)
    #     # nam -= nam
    #     break

    # if nam > 0:
    #     list.append(i)
    # else:
    #     list.append(don)
    #     break

    # if i < 4:
    #     i += 1
    # if i == 4:
    #     list.append(i)
    #     nam -= i
    # if i != 4:
    #     don = 4 - i
    #     i += don
    #     list.append(i)
    #     nam -= don

# for x in range(num):
    # for i in state:
    #     # if i < 4:
    #     #     i += 1
    #     if i == 4:
    #         list.append(i)
    #         nam -= i
    #     if i != 4:
    #         don = 4 - i
    #         i += don
    #         list.append(i)
    #         nam -= i
    # w1 += 1
    # nam -= 1
    # if w1 == 4:
    #     list.append(w1)
    #     # nam -= w1
    #     w1 = 0
if nam == 0 and sum(list) % 4 != 0:
    # list.append(w1)
    print(f"The lift has empty spots!")
    print(*list)
if nam > 0 and sum(list) % 4 == 0:
    # list.append(w1)
    print(f"There isn't enough space! {nam} people in a queue!")
    print(*list)
if nam == 0 and sum(list) % 4 == 0:
    print(*list)



# print(num)
# print(state)
# print(list)
# print(sum(list))



