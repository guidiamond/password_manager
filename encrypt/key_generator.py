import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class KeyGenerator:
    def __init__(self, file, key):
        self.key = key

    def crypt(self, file, message):
        f = Fernet(self.key)
        message = message.encode()
        encrypted = f.encrypt(message)
        with open(file + ".txt", 'wb') as ff:
            ff.write(encrypted)

        with open(file + ".txt", 'rb') as ff:
            fa = ff.read()

        password = self.password_provided.encode() # Convert to type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
        f = Fernet(key)

        decrypted = f.decrypt(fa)
        print(decrypted.decode())
    
    def deccrypt(self, file):
        password = self.password_provided.encode() # Convert to type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
        