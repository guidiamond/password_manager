from zipfile import ZipFile
import os

# ITERAR SOBRE TODOS OS ARQUIVOS TXT DA PASTA
# ADICIONAR A UM ZIP, CASO ELE AINDA NAO TENHA SIDO CRIADO
# ADICIONAR SENHA AO ZIP

class zipfile:
	def __init__(self, directory):
		files_list = os.listdir(directory)

		for file in files_list:
			if file[-3:] == "txt":
				zipfile.add_to_zip(file)	

	def add_to_zip(file):
		if os.access("password.zip", os.R_OK):
			with zipfile.ZipFile('password.zip', 'r') as zip:
				print("dasdas	")

python_manage_pass = zipfile('.')	