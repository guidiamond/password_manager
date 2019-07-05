from .zip_manager import ZipManager
from .read_zip import ReadZip
from .create_zip import CreateZip
from .search import Search
import os
# from  import Interface

class ZipInterface:
    def __init__(self, option):
        manager = ZipManager()
        zip_exists = manager.check_for_zip()
        if not zip_exists:
            manager.create_zip()
        if option == "3":
            manager.add_to_zip()
        elif option == "2":
            zip_files = ReadZip()
            zip_file_names = zip_files.read_zip()
            zip_files.select_file(zip_file_names)
            search_file = input("Type file index or search? (1 | 2) ")
            while search_file not in ("1", "2"):
                search_file = input("Type file index or search? (1 | 2) ")
            if search_file == "2":
                search_word = input("Searched word: ")
                new_zip_file_names = Search(search_word)
                new_zip_file_names = new_zip_file_names.linear_search(zip_file_names)
                zip_files.select_file(new_zip_file_names)
        #     file_name = ReadZip.read_zip()
        #     ReadZip.read_file(file_name)
        return None

# add and read with zip password
# read and write with crpytography
