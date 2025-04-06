import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")

# encrypt
message = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in message:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {message}")
print(f"encrypted message: {cipher_text}")

# decrypt
cipher_text = input("Enter a message to decrypt: ")
message = ""

for letter in cipher_text:
    index = key.index(letter)
    message += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message: {message}")
