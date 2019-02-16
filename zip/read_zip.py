from zipfile import ZipFile
from .create_zip import CreateZip

class ReadZip:
    def read_zip():
            with ZipFile('password.zip', 'r') as zip:
                    ZipFile.printdir(zip)
                    
            print("\nWhich file would you like to see?\n")
            print("press q and enter to quit")
            file_name = input(":")

            #check for input
            while len(file_name.strip()) == 0:
                file_name = input(":")
            if file_name.lower() == "q":
                return None
            return file_name

    def read_file(file_name):
        with ZipFile('password.zip', 'r') as zip:
            try:
                with zip.open(file_name, 'r') as file:
                    vgsdfsda = file.read().decode('UTF-8')
                    print(vgsdfsda.decode('UTF-8'))
            except:
                ReadZip.read_zip()