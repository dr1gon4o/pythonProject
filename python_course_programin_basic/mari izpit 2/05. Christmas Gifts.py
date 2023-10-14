x = input()

g1 = 0
g2 = 0

pod_de = 0
pod_vu = 0

# dete 5 lv
# vuzrasten 15 lv

while True:

    if x == 'Christmas':
        break
    x = int(x)

    if x <= 16:
        g1 += 1
        pod_de += 5
    else:
        g2 += 1
        pod_vu += 15

    x = input()

print(f"Number of adults: {g2}\n" 
f"Number of kids: {g1}\n"
f"Money for toys: {pod_de}\n"
f"Money for sweaters: {pod_vu}"
)
