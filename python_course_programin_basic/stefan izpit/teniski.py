teniska = float(input())
cena = float(input())

c_short = teniska * 0.75
c_socks = c_short * 0.20
c_burons = (teniska + c_short) * 2

total = teniska + c_socks + c_burons + c_short
otstapka = total * 0.15
total_sum = total - otstapka

dif = abs(total_sum - cena)

if cena <= total_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is{total_sum: .2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs{dif: .2f} lv. more.")
