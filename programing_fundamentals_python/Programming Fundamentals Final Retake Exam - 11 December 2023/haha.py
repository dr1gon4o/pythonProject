import re


def decrypt_message(messages):
    for message in messages:
        if re.match(r"[#$%*&][A-Za-z]+[#$%*&]=\d+!![^\s]+", message):
            name = re.findall(r"[#$%*&]([A-Za-z]+)[#$%*&]", message)[0]
            length = int(re.findall(r"=(\d+)!!", message)[0])
            encrypted_code = re.findall(r"!!([^\s]+)", message)[0]
            if length == len(encrypted_code):
                decrypted_code = ''.join(chr(ord(char) + length) for char in encrypted_code)
                return f"Coordinates found! {name} -> {decrypted_code}"

    return "Nothing found!"

input_messages = input()

decrypt_message(input_messages)
