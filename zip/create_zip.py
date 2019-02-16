from zipfile import ZipFile

class CreateZip:

    def check_for_zip():
        try:
            with ZipFile('password.zip', 'r') as zip:
                return 1
        except:
            print("password.zip not found!")
            answer = input("would you like us to create a new one for you? Yes(y) or No (n)")
            while (answer.lower() != "y"):
                answer = input("would you like us to create a new one for you? Yes(y) or No (n)")
            print("chega aqui")    
            return 0

    def create_zip(answer):
        if answer == 1:
            arquivo = ZipFile('password.zip', 'w')
            arquivo.close()
            return None
        return 1