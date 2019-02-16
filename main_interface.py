from zip.zip_interface import ZipInterface

class Interface:

    def __init__(self):
        print("Password Manager 0.1\n")
        # zip_pass = input("Type the key for openning the zip: ")
        # text_pass = input("Type the key to decrpyt password: ")
        zip_pass = 1234
        text_pass = 1234
        print("Options:\n")
        print("1 -> Save new passwords\n")
        print("2 -> See files | passwords\n")
        print("0 -> Exit\n")
        option = input("Option: ")
        while len(option.strip()) == 0:
            option = input("Option: ")
        ZipInterface(option)
        
Interface()