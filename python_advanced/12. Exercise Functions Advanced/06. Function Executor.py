def func_executor(*haha):
    hoho = []

    for x,y in haha:
        hoho.append(f"{x.__name__} - {x(*y)}")
    return "\n".join(hoho)


def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
