def solution():

    def integers():
        for x in range(1, 100000):
            yield x

        #vtori variant
        # num = 1
        #
        # while True:
        #     yield num
        #     num += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for i in range(n)]

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
