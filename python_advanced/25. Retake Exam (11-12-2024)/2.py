
directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

commands = ["up", "down", "left", "right"]
moves = ["S","M","P","R","."]
Resources = 100

n = int(input())
mat = [input().split(" ") for n in range(n)]
last_po = None
start_po = None

move = None
row_index = 0
col_index = 0

for x in range(len(mat)):
    for y in range(len(mat[x])):
        if "s" in y:
            start_po = mat[x][y]

while True:
    pass


# print(mat)
# [print(*el) for el in mat]



# start e S, samo pri dvijenie stava .
# vsiko dvijenie -5
# na R +10
# na +100 e maks
# na Me -5 i stava ot M do '.'
# gubia kogato stane <5 , ili ne moga da stigna P ili R i tova mi last position