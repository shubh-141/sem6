import random

def mod_inv(a, b):
  for i in range(1,b):
    if i*a%b==1:
      return i
  return None


p = 11
q = 17
n = p*q
phi = (p-1)*(q-1)

e = random.randint(1, phi-1)
while mod_inv(e, phi) == None:
  e = random.randint(1, phi-1)
d = mod_inv(e, phi)
print(e,d)
msg = 10
enc_m = int(pow(msg, e, n))
print(enc_m)
dec_m = pow(enc_m, d, n)
print(dec_m)