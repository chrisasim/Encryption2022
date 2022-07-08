import hashlib
hashed_string = hashlib.sha224(b'Hello World!')
hex_digest = hashed_string.hexdisgest()
print(hex_digest)
digest = hashed_string.digest()
hashed_string2 = hashlib.sha512(b'Hello World!')
hex_digest = hashed_string.hexdigest()
print(hex_digest)
print(hashlib.algorithms_available)
