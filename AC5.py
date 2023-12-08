def permutate(key, table):
    return ''.join(key[i - 1] for i in table)
def generate_one_round_key(des_key):
    # Define PC-1
    pc1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
    ]
    # Define PC-2 
    pc2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
    ]

    # Convert the 64-bit key to a binary string
    binary_key = bin(int(des_key, 16))[2:].zfill(64)

    # Apply the PC-1 permutation to the key
    key_after_pc1 = permutate(binary_key, pc1)

    # Split the key inot C and D
    C = key_after_pc1[:28] 
    D = key_after_pc1[28:]

    # Perform circular left shifts based on the round number
    num_shifts = 1
    C = C[num_shifts:] + C[:num_shifts]
    D = D[num_shifts:] + D[:num_shifts] 

    round_key = permutate(C + D, pc2)
    return round_key

# Example usage
des_key = "0x5A2B190E63D0F147" 
round_key = generate_one_round_key(des_key)
print(f"Round 1 Key: {round_key}")
print(f"Round 1 Key: {hex(int(round_key, 2))}")