def encr(a, b):
  pt = input("Enter plain text to be encrypted: ")
  pt = pt.upper()
  ct = ""

  for i in pt:
    if i.isalpha():
      temp1 = (a * (ord(i) - 65) + b) % 26
      temp2 = temp1 + 65
      ct = ct + chr(temp2)

  print("Cipher text - ", ct)

def decr(d, b):
  ct = input("Enter cipher text to be decrypted: ")
  ct = ct.upper()
  pt = ""

  for i in ct:
    if i.isalpha():
      temp1 = (d*((ord(i) - 65) - b)) % 26
      temp2 = temp1 + 65
      pt = pt + chr(temp2)
  print("Plain text - ", pt)

def modInverse(e, phin):
	for d in range(1, phin):
		if (((e % phin) * (d % phin)) % phin == 1):
			return d
	return -1

a = int(input("Enter value of a - "))
b = int(input("Enter value of b - "))

d = modInverse(a, 26)
print("MENU\n1.Encrypt\n2.Decrypt\n3.Exit")
while(True):
  choice = int(input("\nEnter your choice: "))
  if choice == 1:
    encr(a, b)
  elif choice == 2:
    decr(d, b)
  elif choice == 3:
    break
