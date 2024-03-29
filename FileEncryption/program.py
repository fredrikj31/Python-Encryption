from cryptography.fernet import Fernet

def getKey():
	file = open('key.key', 'rb')
	key = file.read()
	file.close()

	print(key)
	
	f = Fernet(key)
	return f

def encryptFile():
	OpenFile = input("What file should be encrypted? >> ")

	try:
		file = open(OpenFile, 'r')
		TextFile = file.read()

		encryptedText = getKey().encrypt(TextFile.encode())

		fileNameExtension = OpenFile.split('.', 1)[0]
		newFileName = fileNameExtension + "-Encrypted" + ".txt"
		createFile = open(newFileName, 'wb')
		createFile.write(encryptedText)
		createFile.close()

		print("File was successfully encrypted!")

	except IOError:
		print("File not found!")

def decryptFile():
	OpenFile = input("What file should be decrypted? >> ")

	try:
		file = open(OpenFile, 'r')
		TextFile = file.read()

		decryptedText = getKey().decrypt(TextFile.encode())

		fileNameExtension = OpenFile.split('-Encrypted', 1)[0]
		newFileName = fileNameExtension + "-Decrypted" + ".txt"
		createFile = open(newFileName, 'w')
		createFile.write(decryptedText.decode())
		createFile.close()

		print("File was successfully decrypted!")

	except IOError:
		print("File not found!")

if __name__ == "__main__":
	print("Welcome to file encryption!")
	print("Please select to encrypt or decrypt a file")
	choose = input("Type (e) for encrypt and (d) for decrypt >> ")
	if choose == "e":
		encryptFile()
	elif choose == "d":
		decryptFile()
	else:
		print("Could not understand that character :(")