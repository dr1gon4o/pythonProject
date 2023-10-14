operant = input()
a = int(input())
b = int(input())


def x(a, b, operant):
    result = None
    if operant == 'multiply':
        result = a + b
    elif operant == 'divide':
        result = int(a / b)
    elif operant == 'add':
        result = a + b
    elif operant == 'subtract':
        result = a - b
    return result

print(x(a, b, operant))
