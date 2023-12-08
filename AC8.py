def generate_public_key(private_key, q, r):
    public_key = [(r * element) % q for element in private_key]
    return public_key

def knapsack_encrypt(plaintext, public_key):
    binary_message = [int(bit) for bit in plaintext]
    if len(binary_message) != len(public_key):
        raise ValueError("Length of the binary message must match the length of the public key")

    encrypted_message = sum(binary_message[i] * public_key[i] for i in range(len(binary_message)))
    return encrypted_message

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the super-increasing sequence (n): "))
    q = int(input("Enter the modulus (q): "))
    r = int(input("Enter the multiplier (r): "))

    # Input the super-increasing sequence
    private_key = [int(input(f"Enter element {i + 1} of the super-increasing sequence: ")) for i in range(n)]

    # Generate the public key
    public_key = generate_public_key(private_key, q, r)

    print("Super-Increasing Sequence (Private Key):", private_key)
    print("Public Key:", public_key)

    plaintext = input("Enter the binary plaintext: ")

    # Encrypt the plaintext using the Knapsack cryptosystem
    ciphertext = knapsack_encrypt(plaintext, public_key)

    print("Original Message:", plaintext)
    print("Encrypted Ciphertext:", ciphertext)


# Number of elements in the super-increasing sequence (n): 8
# Modulus (q): 67
# Multiplier (r): 7
# And your super-increasing sequence is:

# Element 1: 2
# Element 2: 5
# Element 3: 11
# Element 4: 21
# Element 5: 42
# Element 6: 89
# Element 7: 180
# Element 8: 362