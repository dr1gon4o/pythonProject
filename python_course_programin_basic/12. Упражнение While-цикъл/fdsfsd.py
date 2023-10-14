broi_p = int(input())

broi_z = 0
broi_n = 0
all_grade = 0
x = ''
ime = input()

while True:

    if ime != 'Enough':
        grade = int(input())
        broi_z += 1
        all_grade += grade
        x = ime

    ime = input()

    if ime == 'Enough':
        break

    if grade <= 4:
        broi_n += 1

    if broi_n == broi_p:
        break

if broi_n == broi_p:
    print(f"You need a break, {broi_n} poor grades.")
else:
    print(f"Average score: {all_grade / broi_z:.2f}\nNumber of problems: {broi_z}\nLast problem: {x}")
