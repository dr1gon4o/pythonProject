broi_p = int(input())

broi_z = 0
broi_n = 0
all_grade = 0
x = ''

while True:
    ime = input()
    grade = int(input())

    if grade <= 4:
        broi_n += 1

    if broi_n == broi_p:
        print(f"You need a break, {broi_n} poor grades.")
        break

    broi_z += 1
    all_grade += grade
    x = ime

    if ime == 'Enough':
        grade = ""
        print(f"Average score: {all_grade / broi_z:.2f}\nNumber of problems: {broi_z}\nLast problem: {x}")
        break
