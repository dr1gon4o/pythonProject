n = int(input())
#even, odd, negative, positive
numbers = []
filter = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == 'even':
    for number in numbers:
        if number % 2 == 0:
            filter.append(number)
elif command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filter.append(number)
elif command == 'negative':
    for number in numbers:
        if number < 0:
            filter.append(number)
elif command == 'positive':
    for number in numbers:
        if number >= 0:
            filter.append(number)

print(filter)
