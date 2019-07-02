import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from os import path

class NewKeyGenerator:
    def __init__(self, file):
        self.file = file + ".txt"

    def generate_new_key(self, auth_pass):
        # If the path exists dont do anything
        if path.exists(self.file):
            return 0
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
        # Save generated key to file
        with open(self.file, "wb") as ff:
            ff.write(key)

    def read_key(self):
        with open(self.file, "rb") as ff:
            fa = ff.read()
        return fa
