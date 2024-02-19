"""
AES-CBC code
by:Menna Elgaml
"""
#pip install cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def aes_cbc_encrypt(plaintext, key, iv):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()#to have size match the block size
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return ciphertext

def aes_cbc_decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()

    return plaintext

# Generate a random 128-bit key and IV
key = os.urandom(16)
iv = os.urandom(16)

# Input plaintext
plaintext = input("Enter a message to encrypt: ").encode()

# Encrypt plaintext
ciphertext = aes_cbc_encrypt(plaintext, key, iv)
print("Ciphertext:", ciphertext.hex())

# Decrypt ciphertext
decrypted_plaintext = aes_cbc_decrypt(ciphertext, key, iv)
print("Decrypted plaintext:", decrypted_plaintext.decode())
