N = int(input())

grid = []
spaceship_position = None
commands = []

for row in range(N):
    row_data = input().split()
    grid.append(row_data)
    if 'S' in row_data:
        spaceship_position = (row, row_data.index('S'))
        grid[row][spaceship_position[1]] = '.'


# command = input()

while True:
    command = input().strip()
    # command = input()
    if command == "":
        break
    commands.append(command)
    if command == "":
        break
    # command = input()

resources = 100

def is_valid_position(r, c):
    return 0 <= r < N and 0 <= c < N

for command in commands:
    r, c = spaceship_position
    if command == "up":
        r -= 1
    elif command == "down":
        r += 1
    elif command == "left":
        c -= 1
    elif command == "right":
        c += 1

    if not is_valid_position(r, c):
        print("Mission failed! The spaceship was lost in space.")
        break

    sector = grid[r][c]

    if sector == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        grid[r][c] = 'S'
        break
    elif sector == 'M':
        resources -= 5
        if resources < 0:
            resources = 0
        grid[r][c] = '.'
    elif sector == 'R':
        resources += 10
        if resources > 100:
            resources = 100
    else:
        resources -= 5
        if resources < 0:
            resources = 0

    spaceship_position = (r, c)

else:
    print(f"Mission failed! The spaceship was stranded in space.")

for row in grid:
    print(' '.join(row))
