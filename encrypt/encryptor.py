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
        self.pass_directory = 'password/encrypted/'
    def en_crypt(self, file_name, message):
        message = message.encode()
        encrypted = self.fernet.encrypt(message)
        with open(self.pass_directory + file_name + ".txt", 'wb') as ff:
            ff.write(encrypted)
            
    def de_crypt(self, file_name):
        with open(self.pass_directory + file_name, 'rb') as ff:
            fa = ff.read()
        decrypted_message = self.fernet.decrypt(fa).decode()
        return decrypted_message
