num = int(input())

# 01. Programming Fundamentals Mid Exam Retake = []
hoho = 0
alert = 0

for i in range(1, num +1):
    list = input().split()
    # print(list)

    # if len(list[0]) > int(list[1]):
    #     hoho += len(list[0]) - int(list[1])
    if len(list[0]) < int(list[1]):
        dodo = int(list[1]) - len(list[0])
        print(f"{dodo} more chairs needed in room {i}")
    else:
        hoho += len(list[0]) - int(list[1])
        alert += 1



    # 01. Programming Fundamentals Mid Exam Retake.append(list)

# print(01. Programming Fundamentals Mid Exam Retake)
if alert == num:
    print(f"Game On, {hoho} free chairs left")
