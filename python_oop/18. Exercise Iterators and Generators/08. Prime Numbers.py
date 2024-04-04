from math import sqrt


def get_primes(nums):

    for x in nums:
        prime = True
        if x <= 1:
            continue

        for i in range(2, int(sqrt(x) + 1)):
            if x % i == 0:
                prime = False
                break

        if prime:
            yield x



print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))