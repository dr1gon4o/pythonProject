text = input()

glasni = [x for x in text if x.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(glasni))



#vtori varant

# text = input()
# vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
# no_vowels = ''.join([x for x in text if x not in vowels])
# print(no_vowels)