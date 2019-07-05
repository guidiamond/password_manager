import os
from os import path
from zipfile import ZipFile

class ZipManager:
    def __init__(self):
        self.directory = 'password/'
        self.zip_location = os.path.join(self.directory, 'password.zip')

    def check_for_zip(self):
        if path.exists(self.zip_location):
            return 1
        else:
            return 0

    def create_zip(self):
        arquivo = ZipFile(self.zip_location, 'w')
        arquivo.close()
        
    def add_to_zip(self):
        encrypted_path = os.path.join(self.directory + "encrypted/")
        files_list = os.listdir(encrypted_path)
        for file in files_list:
            file_location = os.path.join(encrypted_path, file)

            if file[-3:] == "txt":
                with ZipFile(self.zip_location, 'a') as zip:
                    if file not in zip.namelist():
                        zip.write(file_location, file)
                        os.remove(encrypted_path + file)