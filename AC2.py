def encrypt(sentence):
    # Function to get the unique key for a word
    def get_unique_key(word):
        # Count the number of letters (case-insensitive) in the word
        return sum(char.isalpha() for char in word)

    # Function to encrypt a single character
    def encrypt_char(char, unique_key, common_key):
        if char.isalpha():
            # map 'a' to 0, 'b' to 1, and so on
            char_index = ord(char.lower()) - ord('a')
            # Encryption formula: (char_index * unique_key + common_key) % 26
            encrypted_index = (char_index * unique_key + common_key) % 26
            # map back to alphabet
            encrypted_char = chr(encrypted_index + ord('a'))
            # Maintain the case of the original character
            return encrypted_char.upper() if char.isupper() else encrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            return char

    # Function to perform transposition within a word
    def transpose_word(word):
        # Reverse the order of characters within the word
        return word[::-1]

    # Split the sentence into words
    words = sentence.split()

    # Initialize an empty list to store encrypted words
    encrypted_words = []

    # Common key is the number of words in the sentence
    common_key = len(words)

    # Iterate through each word in the sentence
    for word in words:
        # Get unique key for the word
        unique_key = get_unique_key(word)
        # Encrypt each character in the word
        encrypted_word = ''.join(encrypt_char(char, unique_key, common_key) for char in word)
        # Transpose the encrypted word
        transposed_word = transpose_word(encrypted_word)
        # Add the transposed word to the list
        encrypted_words.append(transposed_word)

    # Join the encrypted words to form the encrypted sentence
    encrypted_sentence = ' '.join(encrypted_words)
    return encrypted_sentence

def decrypt_sentence(sentence):
    return sentence
def decrypt(encrypted_sentence):
    # Function to reverse the transposition within a word
    def reverse_transpose_word(word):
        # Reverse the order of characters within the word
        return word[::-1]

    # Function to decrypt a single character
    def decrypt_char(char, unique_key, common_key):
        if char.isalpha():
            # map 'a' to 0, 'b' to 1, and so on
            char_index = ord(char.lower()) - ord('a')
            # Decryption formula: (char_index - common_key) * modinv(unique_key, 26) % 26
            decrypted_index = (char_index - common_key) * modinv(unique_key, 26) % 26
            # ]\\\ back to alphabet
            decrypted_char = chr(decrypted_index + ord('a'))
            # Maintain the case of the original character
            return decrypted_char.upper() if char.isupper() else decrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            return char

    # Function to calculate the modular inverse
    def modinv(a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    # Function to get the unique key for a word
    def get_unique_key(word):
        # Count the number of letters (case-insensitive) in the word
        return sum(char.isalpha() for char in word)

    # Split the encrypted sentence into words
    words = encrypted_sentence.split()

    # Initialize an empty list to store decrypted words
    decrypted_words = []

    # Common key is the number of words in the sentence
    common_key = len(words)

    # Iterate through each word in the encrypted sentence
    for word in words:
        # Reverse the transposition of the word
        reversed_transposed_word = reverse_transpose_word(word)
        # Get unique key for the word
        unique_key = get_unique_key(reversed_transposed_word)
        # Decrypt each character in the word
        decrypted_word = ''.join(decrypt_char(char, unique_key, common_key) for char in reversed_transposed_word)
        # Add the decrypted word to the list
        decrypted_words.append(decrypted_word)

    # Join the decrypted words to form the decrypted sentence
    decrypted_sentence = ' '.join(decrypted_words)
    return decrypted_sentence


# Take user input for the sentence
user_input = input("Enter a sentence: ")

# Example usage
encrypted_sentence = encrypt(user_input)
print("=== Malhar Bonde - 60019210072 ===")
print("\nOriginal Sentence:", user_input)
print("\nEncrypted Sentence:", encrypted_sentence)
encryptedSentence = user_input


decryptedSentence = decrypt_sentence(encryptedSentence)
print("\nDecrypted Sentence:", decryptedSentence)