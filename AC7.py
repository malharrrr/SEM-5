import math

def gcd(a, h):
    temp = 0
    while 1:
        temp = a % h
        if temp == 0:
            return h
        a = h
        h = temp


def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Take input for prime numbers
p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e = e + 1

d = modinv(e, phi)

# Display calculated values
print("Prime numbers (p and q):", p, q)
print("Product (n):", n)
print("Euler's totient (phi):", phi)
print("Public key (e, n):", e, n)
print("Private key (d, n):", d, n)

# Take input message
msg = int(input("Enter the message to encrypt: "))

print("Message data =", msg)

# Encryption c = (msg ^ e) % n
c = pow(msg, e, n) # Use pow with modulo for better performance
print("Encrypted data =", c)

# Decryption m = (c ^ d) % n
m = pow(c, d, n) # Use pow with modulo for better performance
print("Original Message Sent =", m)

# First prime number (p): 17
# Second prime number (q): 19
# The program will calculate n, phi, e, and d based on these prime numbers. Then, let's take a message to encrypt:

# Message to encrypt: 88