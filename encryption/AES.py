from Crypto.Cipher import AES
key ="Sixteen byte key"
plain = "Secrets 16 bytes"
cipher = AES.new(key)
ciphertext = cipher.encrypt(plain)
print(ciphertext)
plaintext = cipher.decrypt(ciphertext)
print(plaintext)
#ciphertext.encode("hex")
#print(ciphertext.encode('utf-8'))
