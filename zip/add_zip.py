class AddToZip:

    def add_to_zip():
        files_list = os.listdir(directory)
        for file in files_list:
            if file[-3:] == "txt":
                with ZipFile('password.zip', 'a') as zip:
                    zip.write(file)
                    print("feito")
