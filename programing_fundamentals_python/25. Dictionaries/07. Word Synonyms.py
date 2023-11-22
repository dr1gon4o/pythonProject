number = int(input())
rechnik = {}

for i in range(number):
    word = input()
    syno = input()

    if word not in rechnik:
        rechnik[word] = []
    rechnik[word].append(syno)

# print(rechnik)

for x in rechnik:
    print(f"{x} - {', '.join(rechnik[x])}")
# print(f"{rechnik[word]} - {rechnik[syno]}")
