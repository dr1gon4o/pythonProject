import sys

naimalkiapalak = sys.maxsize

while True:
    data = input()

    if data == 'Stop':
        break

    vuvedenitechisla = int(data)

    if vuvedenitechisla < naimalkiapalak:
        naimalkiapalak = vuvedenitechisla

print(naimalkiapalak)
