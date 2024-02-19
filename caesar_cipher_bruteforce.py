"""
ceaser cipher bruteforce code
by:Menna Elgaml
"""
#input
plaintext=input("Enter the text:")
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def bruteforce(ciphertext):
    for i in range(1, 25):
        print(f"{i}: {ceaser_decrypt(ciphertext, i)}")

ciphertext=ceaser_encypt(plaintext,key)
plaintext=ceaser_decrypt(ciphertext, key)
bruteforce_choice = input("Do you want to bruteforce the text? (yes/no): ")
if bruteforce_choice.lower() == 'yes':
    bruteforce(ciphertext)
