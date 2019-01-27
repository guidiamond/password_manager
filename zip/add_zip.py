def add_to_zip(file):

        with ZipFile('password.zip', 'a') as zip:
            zip.write(file)
            print("feito")
    