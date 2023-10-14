pro_maznini = int(input())
pro_proteini = int(input())
pro_vuglexidrat = int(input())
obsht_kalori = int(input())
pro_voda = int(input())

broi_maznini = (pro_maznini * obsht_kalori / 100) / 9
broi_proteini = (pro_proteini * obsht_kalori / 100) / 4
broi_vuglexidrat = (pro_vuglexidrat * obsht_kalori / 100) / 4

teglo = broi_maznini + broi_proteini + broi_vuglexidrat
edin_gram_kalori = obsht_kalori / teglo

# obsht_bori_gramove =

kalori = edin_gram_kalori - (edin_gram_kalori * pro_voda / 100)

# print(broi_maznini, broi_proteini, broi_vuglexidrat)
print(f'{kalori:.04f}')
