import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encryptor:
    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(key)

    def en_crypt(self, file_name, message):
        message = message.encode()
        encrypted = self.fernet.encrypt(message)
        with open(file_name + ".txt", 'wb') as ff:
            ff.write(encrypted)
            
    def de_crypt(self, file_name):
        with open(file_name + ".txt", 'rb') as ff:
            fa = ff.read()
        decrypted_message = self.fernet.decrypt(fa)
        print(decrypted_message.decode())
