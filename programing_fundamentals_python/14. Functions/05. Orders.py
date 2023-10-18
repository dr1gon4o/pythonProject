product = input()
piece = int(input())

def total_price(product, piece):
    result = None
    if product == 'coffee':
        result = piece * 1.50
    elif product == 'water':
        result = piece * 1.00
    elif product == 'coke':
        result = piece * 1.40
    elif product == 'snacks':
        result = piece * 2.0
    return result

print(f'{total_price(product,piece):.02f}')

