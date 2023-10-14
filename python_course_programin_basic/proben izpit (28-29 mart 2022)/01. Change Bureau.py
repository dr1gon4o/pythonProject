bitcoin = int(input())
yoan = float(input())
kom = float(input())

#levove
ce_bit = bitcoin * 1168
ce_yo = yoan * 1.76 * 0.15
#evro
ob_euro = (ce_bit + ce_yo)/ 1.95
pari = ob_euro - (ob_euro * kom / 100)

print(f'{pari:.02f}')
