from zip.zip_interface import ZipInterface
from encrypt.encrypt_interface import EncryptInterface
class Interface:

    def __init__(self):
        print("Password Manager 0.3\n")
        # zip_pass = input("Type the key for openning the zip: ")
        # text_pass = input("Type the key to decrpyt password: ")
        print("Options:\n")
        print("1 -> Save new passwords\n")
        print("2 -> See files | passwords\n")
        print("0 -> Exit\n")
        option = input("Option: ")
        if option == "0":
            import sys
            sys.exit()
        # Check for user input
        while len(option.strip()) == 0:
            option = input("Option: ")
        EncryptInterface(option)
        # ZipInterface(option)

if __name__ == '__main__':
    while True:
        Interface()