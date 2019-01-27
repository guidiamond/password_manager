from zipfile import ZipFile

def read_zip(pass_decrypt):

        with ZipFile('password.zip', 'r') as zip:
            ZipFile.printdir(zip)
        name_file = input("Which file would you like to see? ")
        with ZipFile('password.zip', 'r') as zip:
            with zip.open(name_file, 'r') as file:
                print(file.read())
