from key_generator import KeyGenerator
from new_key_generator import NewKeyGenerator

class EncryptInterface:
    password_provided = input("What is your password? ")
    f = "test"
    key = NewKeyGenerator(f)
    key.generate_new_key(password_provided)
    a = key.read_key()