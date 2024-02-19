"""
RSA algorithm code
by:Menna Elgaml
"""
#make sure numbers is a prime
p=int(input("Enter a prime number(p):"))
q=int(input("enter a prime number(q):"))
from Crypto.Util.number import isPrime
while not isPrime(p):
    print("Please enter a prime number.")
    p = int(input("Enter a prime number: "))
while not isPrime(q):
    print("Please enter a prime number.")
    q = int(input("Enter another prime number: "))
# Encryption and decryption
n=p*q
phi=(p-1) * (q-1)
e = (2**16)+1
d = pow(e, -1, phi)
plaintext = input("Enter a message to encrypt: ")
PT = int.from_bytes(plaintext.encode(), 'big')
CT = pow(PT,e,n)
decrypted = pow(CT, d, n)

# demo
print(f"plaintext: {PT}\nciphertext: {CT}\ndecrypted: {decrypted}")
