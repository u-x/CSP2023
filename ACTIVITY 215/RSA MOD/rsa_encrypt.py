#   a212_rsa_encrypt.py
import rsa as rsa

key = 0
mod = 0
def reqkey():
    global key
    strkey = input("Enter the Encryption Key: " )
    if (strkey.isdigit() != True):
        print("Invalid key. Must be a number.")
        reqkey()
    else:
        key = int(strkey)

def reqmod():
    global mod
    strmod = input("Enter the Modulus: " )
    if (strmod.isdigit() != True):
        print("Invalid modulus. Must be a number.")
        reqmod()
    else:
        mod = int(strmod)

reqkey()
reqmod()
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod, plaintext)
print("Encrypted Message:", encrypted_msg)
