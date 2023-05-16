import hashlib 

st = "GeeksforGeeks"
result = hashlib.sha1(st.encode())
print(result.digest())