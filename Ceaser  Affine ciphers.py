#Ceaser ciphers
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

print(caesar_encrypt("HELLO", 3))

#Affine ciphers

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr(((a * (ord(char)-65) + b) % 26) + 65)
    return result

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""
    for char in cipher:
        if char.isalpha():
            result += chr((a_inv * ((ord(char)-65) - b) % 26) + 65)
    return result