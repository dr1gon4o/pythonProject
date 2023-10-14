x = float(input())

if x <= 10:
    print("slow")

elif 10 < x <= 50:
    print("average")

elif 50 < x <= 150:
    print("fast")

elif 150 < x <= 1000:
    print("ultra fast")

elif x > 1000:
    print("extremely fast")
