# Defining directions for movement
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Reading grid size
N = int(input())

# Initializing variables
grid = []
spaceship_position = None
commands = []
resources = 100

# Reading the grid
for row in range(N):
    row_data = input().split()
    grid.append(row_data)
    if 'S' in row_data:
        spaceship_position = (row, row_data.index('S'))
        grid[row][spaceship_position[1]] = '.'  # Remove 'S' from the grid

# Reading commands
while True:
    command = input().strip()
    if command == "":
        break
    commands.append(command)

# Helper function to check valid position
def is_valid_position(r, c):
    return 0 <= r < N and 0 <= c < N

# Executing commands
for command in commands:
    r, c = spaceship_position

    # Move the spaceship
    dr, dc = directions[command]
    r += dr
    c += dc

    # Check if the position is valid
    if not is_valid_position(r, c):
        print("Mission failed! The spaceship was lost in space.")
        grid[spaceship_position[0]][spaceship_position[1]] = 'S'  # Mark last known position
        break

    # Update position
    current_position = grid[r][c]
    spaceship_position = (r, c)

    # Handle different sectors
    if current_position == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        grid[r][c] = 'S'
        break
    elif current_position == 'M':
        resources -= 10  # 5 for move + 5 for meteorite
        grid[r][c] = '.'
        if resources < 0:
            resources = 0
    elif current_position == 'R':
        resources = min(resources + 10, 100)
    elif current_position == '.':
        resources -= 5  # 5 for move
        if resources < 0:
            print(f"Mission failed! The spaceship was stranded in space.")
            grid[r][c] = 'S'
            break

# Printing the final state of the grid
for row in grid:
    print(' '.join(row))
