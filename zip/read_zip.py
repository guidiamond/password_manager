from zipfile import ZipFile
from .create_zip import CreateZip
import os
class ReadZip:
    def __init__(self):
        self.zip_location = os.path.join('password/', 'password.zip')
        with ZipFile(self.zip_location, 'r') as zip:
            self.zip = zip
    def read_zip_names(self):
        return self.zip.namelist()

    def print_zip_files(self, files_list):
        for file in files_list:
            print(file + " " + "[" + str(files_list.index(file)) + "]")

    def read_txt(self, file_name):
        with ZipFile(self.zip_location, 'r') as zip:
            file_output = zip.read(file_name)
        return file_output
    # def read_file(file_name):
    #     with ZipFile('password.zip', 'r') as zip:
    #         try:
    #             with zip.open(file_name, 'r') as file:
    #                 vgsdfsda = file.read().decode('UTF-8')
    #                 print(vgsdfsda.decode('UTF-8'))
    #         except:
    #             ReadZip.read_zip()
