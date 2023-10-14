x = int(input())
x2 = input()

if x2 == 'Monday' or x2 == 'Tuesday' or x2 == 'Wednesday' or x2 == 'Thursday' or x2 == 'Friday' or x2 == 'Saturday':
    if 10 <= x <= 18 :
        print('open')
    else:
        print('closed')
elif x2 == 'Sunday':
    print('closed')
