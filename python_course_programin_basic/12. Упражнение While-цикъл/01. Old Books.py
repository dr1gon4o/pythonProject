book = input()

broi = 0

while True:
    books = input()

    if books == book:
        print(f"You checked {broi} books and found it.")
        break

    if books != book:
        broi += 1

    if books == 'No More Books':
        broi -= 1
        print(f'The book you search is not here!\nYou checked {broi} books.')
        break
