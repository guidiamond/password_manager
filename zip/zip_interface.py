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
            zip_file_names = zip_files.read_zip_names()
            zip_files.print_zip_files(zip_file_names)
            search_file = input("Type file index or search? (1 | 2) ")
            new_zip_file_names = None
            # Check for valid input
            while search_file not in ("1", "2"):
                search_file = input("Type file index or search? (1 | 2) ")
            # Search mode
            while search_file != "1":
                search_word = input("Search word: ")
                search = Search(search_word)
                new_zip_file_names = search.linear_search(zip_file_names)
                zip_files.print_zip_files(new_zip_file_names)
                search_file = input("Type file index or search? (1 | 2) ")
            file_index = int(input("File index: "))
            if new_zip_file_names == None:
                zip_files.read_txt(zip_file_names[file_index])
            else:
                zip_files.read_txt(new_zip_file_names[file_index])
        #     file_name = ReadZip.read_zip_names()
        #     ReadZip.read_file(file_name)
        return None

# add and read with zip password
# read and write with crpytography
