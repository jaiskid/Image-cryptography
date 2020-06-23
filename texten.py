import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password="pwd"
# encrypt
pyAesCrypt.encryptFile("keys.txt", "keys.txt.aes", password, bufferSize)