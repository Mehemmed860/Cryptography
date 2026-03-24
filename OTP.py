import random

def otp_encrypt(text):
    key = []
    cipher = []

    for i in range(len(text)):
        k = random.randint(0, 25)
        key.append(k)

        value = (ord(text[i]) - 65 + k) % 26
        cipher.append(value)

    return cipher, key


def otp_decrypt(cipher, key):
    result = ""

    for i in range(len(cipher)):
        value = (cipher[i] - key[i]) % 26
        result += chr(value + 65)

    return result


# Example
msg = "HELLO"
cipher, key = otp_encrypt(msg)
print("Cipher:", cipher)
print("Decrypted:", otp_decrypt(cipher, key))