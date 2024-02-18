matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
flatt = []

for sublist in matrix:
    for num in sublist:
        flatt.append(num)

print(flattened)
print(flatt)

#flatt i flattened sa ravni..
#kato se pravi comprehention.. v lioavo sedi vunshnia cikul a ot diasno vutreshnia cikul
