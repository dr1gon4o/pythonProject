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

# Reading the movement commands
while True:
    command = input().strip()
    if command == "":
        break
    commands.append(command)

# Initializing resources
resources = 100


# Helper function to check valid position
def is_valid_position(r, c):
    return 0 <= r < N and 0 <= c < N


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
    if not is_valid_position(r, c):
        print("Mission failed! The spaceship was lost in space.")
        grid[spaceship_position[0]][spaceship_position[1]] = 'S'  # Mark last known position
        break

    # Get the sector at the new position
    sector = grid[r][c]

    # Handle the case where the spaceship reaches Planet B
    if sector == 'P':
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        grid[r][c] = 'S'  # Mark the spaceship's final position
        break

    # Handle meteorite collision
    elif sector == 'M':
        resources -= 10  # 5 for moving, 5 for meteorite
        grid[r][c] = '.'  # Des

else:
    print(f"Mission failed! The spaceship was stranded in space.")

for row in grid:
    print(' '.join(row))