class ReadFiles:
    def read_files():
        with ZipFile('password.zip', 'r') as zip_file:
            return zip_file