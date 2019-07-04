from .encryptor import Encryptor
from .key_generator import KeyGenerator

class EncryptInterface:
    def __init__(self, option):
        # Check for valid input
        if option not in ("1", "2"):
            print("\nWrong Option!\n")
            return None
        # Generate and read key
        key = KeyGenerator()
        key = key.read_key()
        # If key is not saved into a file
        if key == None:
            save_key = None
            # Check for valid input
            while save_key not in ("y", "n"):
                save_key = input("Would you like to save your key in a file? (Y/N) ").lower()
            # Generate key
            key = KeyGenerator()
            key_pass = input("Type the key to read/write the files: ")
            key = key.generate(key_pass, save_key)
        password = Encryptor(key)
        file_name = input("What is the name of the file? ")

        if option == "1":
            message = input("Type your message to be encrypted: ")
            # Pass encryption
            password.en_crypt(file_name, message)
            print("\n###############################\n")
            print("Password Sucessfully Encrypted!")
            print("\n###############################\n ")
        elif option == "2":
            # Pass decryption
            try:
                print("\n###############################\n")
                print("\tPASSWORD:")
                print("\t" + password.de_crypt(file_name + ".txt"))
                print("\n###############################\n ")
            except:
                print("\t;WRONG KEY!")
                print("\n###############################\n ")
