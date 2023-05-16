pt = input("Enter plain text: ")
k = int(input("Enter key: "))
ct=''
for i in pt:
    ct = ct + chr(((ord(i)+k)-ord('a'))%26+ord('a'))
print("Caesar cipher cipher text: ", ct)
pt2 = ''
for i in ct:
    pt2 = pt2 + chr(((ord(i)-k)-ord('a'))%26+ord('a'))
print("Decrypted text: ", pt2) 

for key in range(26):
    x = ''
    for i in ct:
        x += chr((ord(i)-key-ord('a'))%26+ord('a'))
    print(x,'\n')
