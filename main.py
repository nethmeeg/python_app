from cryptography.fernet import Fernet

f = open("data.txt", "wb")
f.write(b"password = dfatu$4576&#Asd")
f.close()

key = Fernet.generate_key()
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)   

def encrypt(key):

    t = Fernet(key)
    with open('data.txt', 'rb') as original_file:
        original = original_file.read()

    encrypted = t.encrypt(original)

    with open ('enc_data.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt(key):
    t = Fernet(key)
    with open('enc_data.txt', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = t.decrypt(encrypted)

    with open('dec_data.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)



encrypt(key)
decrypt(key)
