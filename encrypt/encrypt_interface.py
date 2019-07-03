from .encryptor import Encryptor
from .key_generator import KeyGenerator

class EncryptInterface:
    def __init__(self, option):
        if option not in ("0", "1", "2"):
            print("\nWrong Option!\n")
            return None
        key = KeyGenerator()
        key = key.read_key()
        if key == None:
            save_key = None
            while save_key not in ("y", "n"):
                save_key = input("Would you like to save your key in a file? (Y/N)").lower()
                print(save_key)
            key = KeyGenerator()
            key_pass = input("Type the key to read/write the files: ")
            key = key.generate(key_pass, save_key)
        password = Encryptor(key)
        file_name = input("File name: ")

        if option == "1":
            message = input("Type your message to be encrypted: ")
            # Pass encryption
            password.en_crypt(file_name, message)

        elif option == "2":
            # Pass decryption
            try:
                print(password.de_crypt(file_name + ".txt"))
            except:
                print("Wrong key")