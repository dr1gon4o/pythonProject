line = [int(x) for x in input().split()]
line2 = [int(x) for x in input().split()]

sum = 0
earn = 0
xx = 0
left = 0

for x in range(len(line)):
    sum += line[x]
    sum += line2[x]
    if sum == 10:
        earn += 1
        sum = 0
    elif sum > 10:
        while sum > 10:
            sum = 0
            line2[x] -= 2
            xx += 2
            sum += line[x]
            sum += line2[x]
            if sum == 10:
                earn += 1
                break
            if sum < 10:
                left += sum
                break
        sum = 0
    else:
        left += sum
        sum = 0

# if left > 0:
#     if left
haha = 0
for x in range(left):
    haha += 1
    if haha == 10:
        earn += 1
        haha = 0

if earn >= 7:
    print(f"Great success, you created {earn} earrings.")
else:
    print(f"Keep trying, you need {7 - earn} more earrings.")

# print(line)
# print(line2)
# print(sum)
# print(earn)
