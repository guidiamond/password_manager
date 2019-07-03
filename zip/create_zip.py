from zipfile import ZipFile

class CreateZip:

    def create_zip(answer):
        if answer == 1:
            arquivo = ZipFile('password.zip', 'w')
            arquivo.close()
            return None
        return 1