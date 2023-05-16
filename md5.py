import hashlib 

result = hashlib.md5(b'hello world')
print(result.digest())