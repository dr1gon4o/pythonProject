from itertools import permutations


def possible_permutations(nums):

    all = list(permutations(nums))

    for x in all:
        yield list(x)


[print(n) for n in possible_permutations([1, 2, 3])]
