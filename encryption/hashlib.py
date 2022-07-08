import hashlib
md5 = hashlib.md5()
print(md5)
md5.update(b'Python')
print(md5.digest())
print(md5.hexdigest())
sha = hashlib.sha1(b'Python').hexdigest()
print(sha)
print(hashlib.algorithms_available)
