import random

def generate_keys():
    p, q = 61, 53
    n = p * q
    phi = (p-1)*(q-1)
    e = 17

    def modinv(a, m):
        for x in range(1, m):
            if (a*x) % m == 1:
                return x

    d = modinv(e, phi)
    return (e, n), (d, n)

def encrypt(msg, pub):
    e, n = pub
    return [pow(ord(c), e, n) for c in msg]

def decrypt(cipher, priv):
    d, n = priv
    return ''.join(chr(pow(c, d, n)) for c in cipher)