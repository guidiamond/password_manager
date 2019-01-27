from . import read_zip, add_zip
# from read_zip import read_zip
import os

class zipfile:
    def __init__(self, directory, interface_option, zip_key, pass_decrypt):
        if interface_option == 1:
            pass
            # files_list = os.listdir(directory)
            # for file in files_list:
            #     if file[-3:] == "txt":
            #         read_zip.add_to_zip(file)
        elif interface_option == 2:
            read_zip.read_zip(pass_decrypt)
                # os.remove(file)

# correct b' at start of reading files
# add and read with zip password
# read and write with crpytography