import re

line = input()

while True:

    if re.match(r"[#$%*&][A-Za-z]+[#$%*&]=\d+!![^\s]+", line):
        name = re.findall(r"[#$%*&]([A-Za-z]+)[#$%*&]", line)[0]
        length = int(re.findall(r"=(\d+)!!", line)[0])
        encrypted_code = re.findall(r"!!([^\s]+)", line)[0]
        if length == len(encrypted_code):
            decrypted_code = ''.join(chr(ord(char) + length) for char in encrypted_code)
            print(f"Coordinates found! {name} -> {decrypted_code}")
            break
    else:
        print("Nothing found!")

    line = input()

# else:
#     print("Nothing found!")

# name = 0
# length = 0
# code = 0
# is_found = False
#
# x1 = re.search(name, line)
# x2 = re.search(length, line)
# x3 = re.search(code, line)

# if is_found:
#     print(f"Coordinates found! {nameOfRacer} -> {geohashcode}")
# else:
#     print("Nothing found!")
