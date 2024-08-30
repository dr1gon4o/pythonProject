x, y = input().split()
# string = input() #".", "B", "P".
# mat = [i for i in range(x)]
mat = []
for i in range(int(x)):
    string = input()
    haha= []
    mat.append(haha)
    for o in string:
        haha.append(o)

command = input()  #LRRULUD
moves = []
for y in command:
    moves.append(y)



print(x)
print(y)
# print(mat)
[print(*i) for i in mat]

print(command)
print(moves)
# print(f"dead: {row} {col}")
# print(f"won: {row} {col}")


# word = 'Perfect'
# new_word = word[-1] + word[1:-1] + word[0]
# print(new_word)
# print(word[-1])
# print(word[1:-1])
# print(word[0])