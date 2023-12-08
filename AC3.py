# Function to find the modular multiplicative inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to encrypt text using the Affine cipher
def affine_encrypt(text, a, b):
    result = ""
    m = 26  

    for char in text:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                encrypted_char = chr((a * x + b) % m + ord('a'))
            else:
                x = ord(char) - ord('A')
                encrypted_char = chr((a * x + b) % m + ord('A'))
        else:
            encrypted_char = char  
        result += encrypted_char

    return result

# Function to decrypt text using the Affine cipher
def affine_decrypt(text, a, b):
    result = ""
    m = 26  

    a_inverse = mod_inverse(a, m)
    if a_inverse is None:
        return "The key 'a' is not valid for decryption."

    for char in text:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                decrypted_char = chr((a_inverse * (x - b)) % m + ord('a'))
            else:
                x = ord(char) - ord('A')
                decrypted_char = chr((a_inverse * (x - b)) % m + ord('A'))
        else:
            decrypted_char = char  
        result += decrypted_char

    return result

# Get user input for 'a', 'b', and the text to be encrypted or decrypted
a = int(input("Enter the value of k1:"))
b = int(input("Enter the value of k2:"))
input_text = input("Enter the text to be encrypted:")

# Example
encrypted_text = affine_encrypt(input_text, a, b)
print("Encrypted Text:", encrypted_text)

decrypted_text = affine_decrypt(encrypted_text, a, b)
print("Decrypted Text:", decrypted_text)
