from collections import Counter
import string

ciphertext = """xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpit
ghlxiwiwtxgqadds""".replace("\n", "")

# English letter frequency (most common letters)
english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# Step 1: Frequency count
def frequency_analysis(text):
    freq = Counter(text)
    total = sum(freq.values())
    
    print("Letter Frequencies:")
    for char, count in freq.most_common():
        print(f"{char}: {count} ({count/total:.2f})")

    return freq

# Step 2: Caesar decrypt function
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    return result

# Step 3: Try all shifts (brute force)
def crack_caesar(ciphertext):
    print("\nTrying all possible shifts:\n")
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted}")

# Run everything
freq = frequency_analysis(ciphertext)
crack_caesar(ciphertext)