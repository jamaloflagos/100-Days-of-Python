import string

alphabets = list(string.ascii_lowercase)
print(alphabets)
direction = input("Type \'encode\' to encrypt, type \'decode\' to decrypt:\n").lower()
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""

    for letter in plain_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        if new_position > len(alphabets):
            alphabets.extend(alphabets)
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    
    print(f"The encoded text is {cipher_text}")

def decrypt(cypher_text, shift_amount):
    plain_text = ""

    for letter in cypher_text:
        position = alphabets.index(letter)
        new_position = position - shift_amount
        new_letter = alphabets[new_position]
        plain_text += new_letter

    print(f"The decoded text is {plain_text}")

if direction == 'encode':
    encrypt(plain_text=message, shift_amount=shift)
elif direction == 'decode':
    decrypt(cypher_text=message, shift_amount=shift)