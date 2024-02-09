line = [char for char in input()]
line.sort()

# seto = set(line)
seto2 = tuple(line)

# for char in seto:
#     seto2.
#
# for char in seto2.items():
#     if char in seto:
#         print(f'{char}: {seto2.count(char)} time/s')
#         line.pop(char)

nums_and_occurances = {}
for num in seto2:
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0
    nums_and_occurances[num] += 1

# print(seto)
# print(seto2)
[print(f"{key}: {value} time/s") for key, value in
nums_and_occurances.items()]
