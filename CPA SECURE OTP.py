from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Step 1: Generate a random key
def generate_key():
    key = get_random_bytes(16)  # 16 bytes = 128-bit key
    print("Generated Key:", key)
    return key


# Step 2: Encrypt the message
def encrypt_message(message, key):
    print("\n--- Encryption ---")
    
    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CTR)
    
    print("Nonce:", cipher.nonce)
    
    # Convert message to bytes
    message_bytes = message.encode()
    print("Message in bytes:", message_bytes)
    
    # Encrypt
    ciphertext = cipher.encrypt(message_bytes)
    print("Ciphertext:", ciphertext)
    
    return cipher.nonce, ciphertext


# Step 3: Decrypt the message
def decrypt_message(nonce, ciphertext, key):
    print("\n--- Decryption ---")
    
    # Recreate cipher with same key + nonce
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    
    # Decrypt
    decrypted_bytes = cipher.decrypt(ciphertext)
    print("Decrypted bytes:", decrypted_bytes)
    
    # Convert back to string
    decrypted_message = decrypted_bytes.decode()
    
    return decrypted_message


# Step 4: Run everything
key = generate_key()

message = "HELLO CRYPTO"

nonce, ciphertext = encrypt_message(message, key)

decrypted = decrypt_message(nonce, ciphertext, key)

print("\nFinal Decrypted Message:", decrypted)