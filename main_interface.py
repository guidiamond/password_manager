from zip.zip_interface import ZipManager

class Interface:

    def __init__(self):
        print("Password Manager 0.1\n")
        # zip_key = input("Type the key for openning the zip: ")
        # pass_decrypt = input("Type the key to decrpyt password: ")
        zip_key = 1234
        pass_decrypt = 1234
        print("Options:\n")
        print("1 -> Save new passwords\n")
        print("2 -> See files | passwords\n")
        print("3 -> Push from cloud\n")
        print("0 -> Exit\n")
        opcao = input("Opcao: ")
        while len(opcao.strip()) == 0:
            opcao = input("Opcao: ")
        ZipManager('.', opcao)
Interface()