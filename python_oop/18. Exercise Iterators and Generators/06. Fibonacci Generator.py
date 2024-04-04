def fibonacci():
    num1, num2 = 0, 1

    while True:
        yield num1

        num1, num2 = num2, num1 + num2

    # result1 = 0
    # result2 = 0
    # x = 0
    # x2 = 1
    #
    # for i in range(n):
    #     x3 = x + x2
    #     result1 += x3
    # # x4 = next(haha) *2
    #     yield result1
    #     result2 += x2 + result1
    #     yield result2
    #     result2 += result1 + result2
    #     yield

generator = fibonacci()
for i in range(5):
    print(next(generator))
