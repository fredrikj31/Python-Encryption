import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def getKey(password):
	password_provided = password # This is input in the form of a string
	password = password_provided.encode() # Convert to type bytes
	salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(password))

	f = Fernet(key)

	return f

def encryptFile():
	OpenFile = input("What file should be encrypted? >> ")
	CryptPassword = input("Enter the password to encrypt this file >> ")

	try:
		file = open(OpenFile, 'r')
		TextFile = file.read()

		encryptedText = getKey(CryptPassword).encrypt(TextFile.encode())

		fileNameExtension = OpenFile.split('.', 1)[0]
		newFileName = fileNameExtension + "-Encrypted" + ".txt"
		createFile = open(newFileName, 'wb')
		createFile.write(encryptedText)
		createFile.close()

		print("File was successfully encrypted!")

	except IOError:
		print("File not found!")
		exit()

def decryptFile():
	OpenFile = input("What file should be decrypted? >> ")
	CryptPassword = input("Enter the password to encrypt this file >> ")

	try:
		file = open(OpenFile, 'r')
		TextFile = file.read()

		try:
			decryptedText = getKey(CryptPassword).decrypt(TextFile.encode())
		except:
			print("Wrong password to unlock file.")
			exit()

		fileNameExtension = OpenFile.split('-Encrypted', 1)[0]
		newFileName = fileNameExtension + "-Decrypted" + ".txt"
		createFile = open(newFileName, 'w')
		createFile.write(decryptedText.decode())
		createFile.close()

		print("File was successfully decrypted!")

	except IOError:
		print("File not found!")
		exit()

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