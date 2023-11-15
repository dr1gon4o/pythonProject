wagons = [0] * int(input())
# command = input().split()
while True:
    command = input().split()

    if command[0] == 'End':
        print(wagons)
        break

    if command[0] == 'add':
        ppl = int(command[1])
        wagons[-1] += ppl

    elif command[0] == 'insert':
        index = int(command[1])
        ppl = int(command[2])
        wagons[index] += ppl

    elif command[0] == 'leave':
        index = int(command[1])
        ppl = int(command[2])
        wagons[index] -= ppl

    # command = input().split(' ')
