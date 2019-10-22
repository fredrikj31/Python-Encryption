from cryptography.fernet import Fernet

message = "my deep dark secret".encode()

def getKey():
	file = open('key.key', 'rb')
	key = file.read()
	file.close()
	return key

def encryptFile():
	OpenFile = input("What file should be encrypted? >> ")

	print(OpenFile)

	f = Fernet(getKey())

	try:
		file = open(OpenFile, 'r')
		TextFile = file.read()
		print(TextFile)

		encryptedText = f.encrypt(TextFile)

		fileNameExtension = OpenFile.split('.', 1)[0]
		newFileName = fileNameExtension + "-Encrypted" + ".txt"
		createFile = open(newFileName, 'wb')
		createFile.write(encryptedText)
		createFile.close()

	except IOError:
		print("File not found!")

def decryptFile():
	f = Fernet(getKey())
	encrypted = b"gAAAAABdrzbL-eRX8LhDZZyXzXjQfw5yYYUTKjDTNHjqP0DRNVeZWBfO5TSyFumhEMfGLb8eA1YBKabba1fUAkPPr6WQd5aZVVZ1ppdHXBKkEsZrgstOlIM="
	decrypted = f.decrypt(encrypted)

	print(decrypted.decode())

encryptFile()