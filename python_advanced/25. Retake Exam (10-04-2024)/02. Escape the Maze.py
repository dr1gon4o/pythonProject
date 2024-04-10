def escape_the_maze(n, matrix, **commands):
    health = 100
    player_pos = [0, 0]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'P':
                player_pos = [i, j]
                break
        if matrix[player_pos[0]][player_pos[1]] == 'P':
            break

    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "right": (0, 1),
        "left": (0, -1),
    }
    for command in commands:
        delta = moves[command]
        new_pos = [player_pos[0] + delta[0], player_pos[1] + delta[1]]

        if 0 <= new_pos[0] < n and 0 <= new_pos[1] < n:

            cell = matrix[new_pos[0]][new_pos[1]]

            if cell == 'M':
                health -= 40
                if health <= 0:
                    matrix[player_pos[0]][player_pos[1]] = '-'
                    break
                matrix[new_pos[0]][new_pos[1]] = 'P'
            elif cell == 'H':
                health = min(100, health + 15)
                matrix[new_pos[0]][new_pos[1]] = 'P'
            elif cell == 'X':
                matrix[player_pos[0]][player_pos[1]] = '-'
                matrix[new_pos[0]][new_pos[1]] = 'P'
                break
            else:
                matrix[new_pos[0]][new_pos[1]] = 'P'

            if player_pos != new_pos:
                matrix[player_pos[0]][player_pos[1]] = '-'
                player_pos = new_pos

    if health > 0 and matrix[player_pos[0]][player_pos[1]] == 'P':
        outcome = "Player escaped the maze. Danger passed!"
    else:
        outcome = "Player is dead. Maze over!"

    final_maze = "\n".join("".join(row) for row in matrix)

    return outcome, f"Player's health: {health} units", final_maze






