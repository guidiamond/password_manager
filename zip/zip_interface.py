from .add_zip import AddToZip
from .read_zip import ReadZip
from .create_zip import CreateZip
import os
# from  import Interface

class ZipInterface:
    def __init__(self, option):
        if option == "1":
            AddToZip.add_to_zip()
        elif option == "2":
            check = CreateZip.check_for_zip()
            CreateZip.create_zip(check)
            file_name = ReadZip.read_zip()
            ReadZip.read_file(file_name)
        elif option == "0":
            return None
        return None

# add and read with zip password
# read and write with crpytography