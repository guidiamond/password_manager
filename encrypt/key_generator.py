import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class KeyGenerator:
    def __init__(self, key):
        self.key = key
        self.f = Fernet(self.key)

    def crypt(self, file_name, message):
        message = message.encode()
        encrypted = self.f.encrypt(message)
        with open(file_name + ".txt", 'wb') as ff:
            ff.write(encrypted)
        print("ok")
    def deccrypt(self, file):
        with open(file + ".txt", 'rb') as ff:
            fa = ff.read()

        decrypted = self.f.decrypt(fa)
        print(decrypted.decode())