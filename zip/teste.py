import ruamel.std.zipfile as zipfile

zipfile.delete_from_zip_file('password.zip', file_names=['a.txt'])
