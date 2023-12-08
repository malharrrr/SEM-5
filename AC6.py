def permutate(key, table):
    return ''.join(key[i - 1] for i in table if 0 < i <= len(key))
def generate_one_round_key(des_key):
    pc1 = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
    ]
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

def initial_permutation(text):
    # Initial permutation (IP) table
    ip_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    return permutate(text, ip_table)

def expansion_permutation(text):
    # Expansion permutation (E) table
    e_table = [
        32, 1, 2, 3, 4, 5, 4, 5,
        6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27,
        28, 29, 28, 29, 30, 31, 32, 1
    ]
    return permutate(text, e_table)

def substitution_boxes(text):
    # Define the S-boxes
    s_boxes = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    # Split the 48-bit input into 6-bit blocks
    blocks = [text[i:i+6] for i in range(0, len(text), 6)]

    # Apply the S-boxes
    result = ''
    for i, block in enumerate(blocks):
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        value = s_boxes[i][row][col]
        result += format(value, '04b')

    return result

def permutation(text):
    # Permutation (P) table
    p_table = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]
    return permutate(text, p_table)

def f_function(right_half, round_key):
    # Expansion permutation
    expanded_right = expansion_permutation(right_half)

    # XOR with round key
    xor_result = bin(int(expanded_right, 2) ^ int(round_key, 2))[2:].zfill(48)

    # S-box substitution
    substituted = substitution_boxes(xor_result)

    # Permutation
    permuted = permutation(substituted)

    return permuted

def des_encrypt(plain_text, des_key):
    # Initial permutation
    text_after_ip = initial_permutation(plain_text)

    # Split the text into left and right halves
    left_half = text_after_ip[:32]
    right_half = text_after_ip[32:]

    print("Initial Round 0:")
    print(f"Left Half: {left_half}")
    print(f"Right Half: {right_half}\n")

    # Perform 16 rounds of DES
    for round_num in range(1, 17):
        round_key = generate_one_round_key(des_key)

        print(f"Round {round_num}:")
        print(f"Round Key: {round_key}")

        # F function
        f_result = f_function(right_half, round_key)

        # XOR with left half
        xor_result = bin(int(left_half, 2) ^ int(f_result, 2))[2:].zfill(32)

        print(f"Left Half: {right_half}")
        print(f"Right Half: {xor_result}\n")

        # Update left and right halves for the next round
        left_half = right_half
        right_half = xor_result

    # Final permutation (inverse of initial permutation)
    # Final permutation (inverse of initial permutation)
    encrypted_text = permutate(right_half + left_half, [40, 8, 48, 16, 56, 24, 64, 32,
                                                      39, 7, 47, 15, 55, 23, 63, 31,
                                                      38, 6, 46, 14, 54, 22, 62, 30,
                                                      37, 5, 45, 13, 53, 21, 61, 29,
                                                      36, 4, 44, 12, 52, 20, 60, 28,
                                                      35, 3, 43, 11, 51, 19, 59, 27,
                                                      34, 2, 42, 10, 50, 18, 58, 26,
                                                      33, 1, 41, 9, 49, 17, 57, 25])

    print("Final Round (After 16 Rounds):")
    print(f"Left Half: {left_half}")
    print(f"Right Half: {right_half}\n")

    return encrypted_text
plain_text_hex = input("Enter plaintext (hex): ").strip()
des_key_hex = input("Enter DES key (hex): ").strip()

# Convert hexadecimal strings to binary
plain_text_bin = bin(int(plain_text_hex, 16))[2:].zfill(64)
des_key_bin = bin(int(des_key_hex, 16))[2:].zfill(64)

# Call the des_encrypt function with user input
encrypted_text = des_encrypt(plain_text_bin, des_key_bin)

print(f"Encrypted Text: {encrypted_text}")
print(f"Encrypted Text (Hex): {hex(int(encrypted_text, 2))[2:]}")

# Plain Text (hex): "0x0123456789ABCDEF"
# DES Key (hex): "0x133457799BBCDFF1"