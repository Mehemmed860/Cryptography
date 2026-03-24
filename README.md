Cryptography Algorithms in Python

This repository contains implementations of fundamental cryptographic algorithms written in Python.
The goal of this project is to understand both the theory and practical implementation of classical and modern cryptography techniques.

📌 Contents
GCD (Euclidean Algorithm)
Caesar Cipher & Affine Cipher
One-Time Pad (OTP)
OTP with PRG
Frequency Analysis Attack
CPA-Secure Encryption (AES-based)
Extended Euclidean Algorithm
RSA Encryption
Diffie-Hellman Key Exchange
PRG based on Discrete Log
⚙️ Requirements
Python 3.x
PyCryptodome library (for AES)

Install required library:

pip install pycryptodome
📖 Project Explanation

1. GCD (Greatest Common Divisor)
Uses Euclidean Algorithm
Finds the greatest common divisor of two integers
Important for modular arithmetic and cryptography
2. Caesar Cipher
A simple substitution cipher
Each letter is shifted by a fixed number

Example:

HELLO → KHOOR (shift = 3)
Affine Cipher
More advanced substitution cipher
Formula:
E(x) = (a * x + b) mod 26
3. One-Time Pad (OTP)
Perfectly secure encryption method (theoretically)
Uses a random key equal to message length

Encryption:

C = (P + K) mod 26

Decryption:

P = (C - K) mod 26

4. OTP + PRG
Instead of truly random key, uses a pseudo-random generator (PRG)
Key is generated using a seed

⚠️ Note: Not perfectly secure like real OTP

5. Frequency Analysis Attack
Breaks Caesar cipher using letter frequency
English language has known frequency patterns
Only 1 most frequent letter is enough to guess the key

6. CPA-Secure Encryption (AES)
Uses AES in CTR mode
Provides security against chosen-plaintext attacks

Steps:

Generate random key
Encrypt message
Decrypt using same key + nonce

7. Extended Euclidean Algorithm
Finds:
gcd(a, b)
coefficients x, y such that:
ax + by = gcd(a, b)

Used in:

Modular inverse
RSA

8. RSA Encryption
Public-key cryptography system

Steps:

Choose primes p and q
Compute n = p * q
Compute φ(n)
Choose e
Compute d

Encryption:

C = M^e mod n

Decryption:

M = C^d mod n

9. Diffie-Hellman Key Exchange
Secure key exchange over insecure channel

Steps:

Choose prime p and generator g
Generate private keys
Exchange public values
Compute shared secret

✔ In this project:

p is generated randomly (prime)

10. PRG based on Discrete Log
Generates pseudo-random bits using modular exponentiation

Formula:

x = g^x mod p
