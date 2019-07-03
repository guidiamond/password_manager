import os
from zipfile import ZipFile

class ZipManager:
    def __init__(self, directory):
        self.directory = directory

    def check_for_zip(self):
        try:
            with ZipFile('password.zip', 'r') as zip:
                return 1
        except:
            print("password.zip not found!")
            answer = input("would you like us to create a new one for you? Yes(y) or No (n)")
            while (answer.lower() != "y"):
                answer = input("would you like us to create a new one for you? Yes(y) or No (n)")
            print("chega aqui")    
            return 0

    def create_zip(self, answer):
        if answer == 1:
            arquivo = ZipFile('password.zip', 'w')
            arquivo.close()
            return None
        return 1
        
    def add_to_zip(self):
        files_list = os.listdir(self.directory)
        print(files_list)
        for file in files_list:
            if file[-3:] == "txt":
                with ZipFile('password.zip', 'a') as zip:
                    zip.write(file)