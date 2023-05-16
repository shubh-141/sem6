from random import randint


p = 23  
g = 5   

a = randint(2, p-2)  
b = randint(2, p-2)  


A = (g ** a) % p     
B = (g ** b) % p     
s_A = (B ** a) % p   
s_B = (A ** b) % p   

assert s_A == s_B

print(f"The shared secret key is {s_A}")