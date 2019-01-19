from zipfile import ZipFile
import os

# ITERAR SOBRE TODOS OS ARQUIVOS TXT DA PASTA
# ADICIONAR A UM ZIP, CASO ELE AINDA NAO TENHA SIDO CRIADO
# ADICIONAR SENHA AO ZIP

class zipfile:
	def __init__(self, directory, interface_option, zip_key, pass_decrypt):
		if interface_option == 1:
			files_list = os.listdir(directory)
			for file in files_list:
				if file[-3:] == "txt":
					zipfile.add_to_zip(file)
		elif interface_option == 2:
			zipfile.read_zip(pass_decrypt)
				# os.remove(file)

	def add_to_zip(file):

		with ZipFile('password.zip', 'a') as zip:
			zip.write(file)
			print("feito")
		
	def read_zip(pass_decrypt):

		with ZipFile('password.zip', 'r') as zip:
			ZipFile.printdir(zip)
		name_file = input("Which file would you like to see? ")
		with ZipFile('password.zip', 'r') as zip:
			with zip.open(name_file, 'r') as file:
				print(file.read())


# correct b' at start of reading files
# add and read with zip password
# read and write with crpytography