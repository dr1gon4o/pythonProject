import sys


def main():

    input_data = sys.stdin.read().splitlines()

    rows, cols = map(int, input_data[0].split(', '))

    game_map = [list(input_data[i + 1]) for i in range(rows)]


    ct_position = None
    bomb_position = None
    terrorists = []
    time_left = 16
    defuse_time = 0
    initial_time_left = time_left


    for r in range(rows):
        for c in range(cols):
            if game_map[r][c] == 'C':
                ct_position = (r, c)
            elif game_map[r][c] == 'B':
                bomb_position = (r, c)
            elif game_map[r][c] == 'T':
                terrorists.append((r, c))


    def print_final_state():
        for row in game_map:
            print(''.join(row))


    def move_ct(direction):
        nonlocal ct_position, time_left
        r, c = ct_position
        if direction == 'left':
            c -= 1
        elif direction == 'right':
            c += 1
        elif direction == 'up':
            r -= 1
        elif direction == 'down':
            r += 1


        if 0 <= r < rows and 0 <= c < cols:
            ct_position = (r, c)
            time_left -= 1
        else:
            time_left -= 1


    def defuse_bomb():
        nonlocal time_left, ct_position, bomb_position
        if ct_position == bomb_position:
            defuse_time = 4
            time_left -= defuse_time
            game_map[bomb_position[0]][bomb_position[1]] = 'D'


    commands = input_data[rows + 1:]
    for command in commands:
        if time_left <= 0:
            print("Terrorists win!")
            print("Bomb was not defused successfully!")
            print(f"Time needed: {initial_time_left - time_left} second/s.")
            break

        if command == "defuse":
            if ct_position == bomb_position:
                defuse_bomb()
                if time_left < 0:
                    print("Terrorists win!")
                    print("Bomb was not defused successfully!")
                    print(f"Time needed: {initial_time_left - time_left} second/s.")
                    break
            else:
                time_left -= 2

        elif command in ['left', 'right', 'up', 'down']:
            move_ct(command)

        if ct_position in terrorists:
            game_map[ct_position[0]][ct_position[1]] = '*'
            print("Terrorists win!")
            break

        if time_left <= 0:
            print("Terrorists win!")
            print("Bomb was not defused successfully!")
            print(f"Time needed: {initial_time_left - time_left} second/s.")
            break

    if game_map[bomb_position[0]][bomb_position[1]] == 'D':
        print("Counter-terrorist wins!")
        print(f"Bomb has been defused: {time_left} second/s remaining.")

    print_final_state()

if __name__ == "__main__":
    main()
