import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import path
from .encryptor import Encryptor

class KeyGenerator:
    def __init__(self):
        self.pass_directory='password/'
    def generate(self, auth_pass, save_key):
        password = auth_pass.encode() # Convert pass to type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'teste',
            iterations=100000,
            backend=default_backend()
        )
        # Key generator
        key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
        # Don't save if user doesn't want to
        if save_key == "n":
            return key
        # Save generated key to file
        with open(self.pass_directory + "key.key", "wb") as ff:
            ff.write(key)
        return key

    def read_key(self):
        # If key exists read it
        if path.exists(self.pass_directory + "key.key"):
            with open(self.pass_directory + "key.key", "rb") as key_file:
                key = key_file.read()
            return key
        else:
            return None
