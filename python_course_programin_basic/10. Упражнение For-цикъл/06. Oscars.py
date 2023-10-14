ime = input()
pointa = float(input())
n = int(input())

result = pointa

for i in range(n):
    imeo = input()
    point = float(input())
    result += len(imeo) * point / 2

    if result >= 1250.5:
        print(f"Congratulations, {ime} got a nominee for leading role with {result:.01f}!")
        break
else:
    print(f"Sorry, {ime} you need {1250.5 - result:.01f} more!")
