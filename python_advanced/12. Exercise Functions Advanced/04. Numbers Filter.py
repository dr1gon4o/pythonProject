def even_odd_filter(**nums):
    # key = nums[0]
    # value = nums[1]

    for x,y in nums.items():
        if x == "even":
            y2 = [x for x in y if x % 2 == 0]
            nums[x] = y2
        else:
            y2 = [x for x in y if x % 2 != 0]
            nums[x] = y2
    return nums

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
