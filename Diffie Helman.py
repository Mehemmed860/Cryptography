import random

# Step 1: Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Step 2: Generate random prime number
def generate_prime(start=10, end=100):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num


# Step 3: Diffie-Hellman
def diffie_hellman():
    print("--- Diffie-Hellman Key Exchange ---")
    
    # Random prime p
    p = generate_prime()
    print("Prime p:", p)
    
    # Generator g (simple choice)
    g = random.randint(2, p-2)
    print("Generator g:", g)
    
    # Private keys
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)
    
    print("Private key a:", a)
    print("Private key b:", b)
    
    # Public values
    A = pow(g, a, p)
    B = pow(g, b, p)
    
    print("Public A:", A)
    print("Public B:", B)
    
    # Shared secrets
    shared1 = pow(B, a, p)
    shared2 = pow(A, b, p)
    
    print("Shared key (Alice):", shared1)
    print("Shared key (Bob):", shared2)
    
    print("Keys match:", shared1 == shared2)


# Run
diffie_hellman()