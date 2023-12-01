

xx = int(input())

sum = 0
for x in range(1, xx +1):
    if xx % x == 0:
        sum += x

if sum == xx * 2:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")


