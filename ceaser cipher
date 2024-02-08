"""
ceaser cipher code
by:Menna Elgaml
"""
#input
plaintext=input("enter a text:")
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#process
def ceaser_encypt(plaintext,key):
    ciphertext=""
    for letter in plaintext:
        ciphertext +=alphabet[(alphabet.index(letter)+key)%26]

    return ciphertext


def ceaser_decrypt(ciphertext,key):
    plaintext = ""
    for letter in ciphertext:
        plaintext += alphabet[(alphabet.index(letter) -key) % 26]

    return plaintext
key=eval(input("enter the key:"))
ciphertext=ceaser_encypt(plaintext,key)
plaintext=ceaser_decrypt(ciphertext, key)
print(f"the encypted text:",ciphertext)#f =format
print(f"the decrypted text:",plaintext)
