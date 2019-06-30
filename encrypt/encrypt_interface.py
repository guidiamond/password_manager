from key_generator import KeyGenerator
from new_key_generator import NewKeyGenerator

class EncryptInterface:
    def __init__(self):
        password_provided = input("What is your password? ")
        file_name = "test"
        key = NewKeyGenerator(file_name)
        key.generate_new_key(password_provided)
        a = key.read_key()
        b = KeyGenerator(a)
        # message = input("Type your message to be encrypted")
        # b.crypt("arquivoA", message)
        b.deccrypt("arquivoA")
EncryptInterface()