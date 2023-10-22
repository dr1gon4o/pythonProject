team_a = []
team_b = []

team_a = ['A-' + str(n) for n in range(1,12)]
team_b = ['B-' + str(n) for n in range(1,12)]

#demek tova stava taka
# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

game_iss_terminated = False

string = input().split()
for player in string:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        game_iss_terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if game_iss_terminated:
    print("Game was terminated")


# tova e vtori vaiant moi.. no e mnogo dulug
# list_a = []
# list_b = []
#
# for n in range(1, 11+1, 1):
#     list_a.append(n)
#     list_b.append(n)
#
# string = input().split()
#
# count_A = 0
# count_B = 0
#
# print(f'Team A - {count_A}; Team B - {count_B}')
# print("Game was terminated")
# print(list_a)
# print(list_b)
