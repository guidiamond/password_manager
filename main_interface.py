from zip.zip_interface import ZipInterface
from encrypt.encrypt_interface import EncryptInterface
class Interface:

    def __init__(self):
        print("Password Manager 0.3\n")
        print("Options:\n")
        print("1 -> Encrypt new file\n")
        print("2 -> READ FILE\n")
        print("3 -> Add Encrypted files to zip\n")
        print("0 -> EXIT\n")
        option = input("Option: ")
        # Exit
        if option == "0":
            import sys
            sys.exit()
        # Check for user input
        while len(option.strip()) == 0:
            option = input("Option: ")
        EncryptInterface(option)
        ZipInterface(option)

if __name__ == '__main__':
    while True:
        Interface()
        wait_for_user = input("Press any key to continue: ")