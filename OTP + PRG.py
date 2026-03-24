import random

def otp_prg_encrypt(text, seed):
    random.seed(seed)

    key = []
    cipher = []

    for i in range(len(text)):
        k = random.randint(0, 25)
        key.append(k)

        value = (ord(text[i]) - 65 + k) % 26
        cipher.append(value)

    return cipher, key


def otp_prg_decrypt(cipher, key):
    result = ""

    for i in range(len(cipher)):
        value = (cipher[i] - key[i]) % 26
        result += chr(value + 65)

    return result


# Example
msg = "HELLO"
cipher, key = otp_prg_encrypt(msg, 42)
print("Cipher:", cipher)
print("Decrypted:", otp_prg_decrypt(cipher, key))