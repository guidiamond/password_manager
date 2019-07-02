from .encryptor import Encryptor
from .new_key_generator import NewKeyGenerator

class EncryptInterface:
    def __init__(self, option):
        if option == "1":
            key_pass = input("Type the key used to read/write the password: ")
            file_name = input("File name: ")
            message = input("Type your message to be encrypted: ")
            # Key read and generation (if needed)
            key = NewKeyGenerator(file_name)
            key.generate_new_key(key_pass)
            key = key.read_key()
            # Pass encryption
            password = Encryptor(key)
            # password.en_crypt(file_name, message)

        elif option == "2":
            password.de_crypt(file_name + ".txt")
