# Reading the grid size
N = int(input())

# Initializing the grid and spaceship position
grid = []
spaceship_position = None
commands = []

# Reading the grid
for row in range(N):
    row_data = input().split()
    grid.append(row_data)
    if 'S' in row_data:
        spaceship_position = (row, row_data.index('S'))
        grid[row][spaceship_position[1]] = '.'  # Removing 'S' from initial position

# Read the movement commands
commands = []
while True:
    try:
        command = input()
        commands.append(command)
    except EOFError:
        break

# Initializing resources
resources = 100


# Helper function to check valid position
def is_valid_position(r, c):
    return 0 <= r < N and 0 <= c < N


# Unpack current position
r, c = spaceship_position

# Get the sector at the new position
sector = grid[r][c]

# Loop through the commands
for command in commands:
    # Unpack current position
    r, c = spaceship_position

    # Update position based on the direction
    if command == "up":
        r -= 1
    elif command == "down":
        r += 1
    elif command == "left":
        c -= 1
    elif command == "right":
        c += 1

    # Check if the new position is out of bounds
    if not is_valid_position(r, c) or resources <= 0:
        print("Mission failed! The spaceship was lost in space.")
        grid[spaceship_position[0]][spaceship_position[1]] = 'S'  # Mark last known position
        break

    # Get the sector at the new position
    sector = grid[r][c]

    # Decrease by 5 resources because of a move
    resources -= 5

    # Handle the case where the spaceship reaches Planet B
    if sector == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break

    # Handle meteorite collision
    elif sector == 'M':
        resources -= 5  # 5 for moving, 5 for meteorite
        grid[r][c] = '.'  # Des

    elif sector == 'R':
        resources += 10
        if resources > 100:
            resources = 100

    spaceship_position = (r, c)
else:
    # If the loop completes without reaching Planet B, it means we ran out of resources
    print("Mission failed! The spaceship was stranded in space.")
    grid[spaceship_position[0]][spaceship_position[1]] = 'S'  # Mark last known position

# Final grid printout
for row in grid:
    print(' '.join(row))