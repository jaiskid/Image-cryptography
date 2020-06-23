import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password="pwd"
# decrypt
pyAesCrypt.decryptFile("keys.txt.aes", "keysout.txt", password, bufferSize)