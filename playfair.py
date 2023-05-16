def to_mat(characters):
  mat=[]
  for i in range(0,len(characters), 6):
    mat.append(characters[i:i+6])
  return mat

pt = input("Enter plaintext: ").lower()
key = input("Enter key: ").lower()
mat = []
for el in key:
  mat.append(el)
for i in range(97, 123):
  if chr(i) not in mat:
    mat.append(chr(i))
for i in range(10):
  if str(i) not in mat:
    mat.append(str(i))
mat = to_mat(mat)
for el in mat:
  print(el)

ct1=[]
if len(pt)%2!=0:
  for i in range(0,len(pt)-1,2):
    if pt[i]!=pt[i+1]:
      ct1.append(pt[i:i+2])
    else:
      ct1.append(pt[i] + 'x')
      ct1.append(pt[i] + 'x')
  ct1.append(pt[-1] + 'x')
else:
  for i in range(0,len(pt),2):
    if pt[i]!=pt[i+1]:
      ct1.append(pt[i:i+2])
    else:
      ct1.append(pt[i] + 'x')
      ct1.append(pt[i] + 'x')

ct=[]
for i in ct1:
  ind1=0
  ind2=0
  for j in range(len(mat)):
    if i[0] in mat[j]:
      ind1=[j, mat[j].index(i[0])]
    if i[1] in mat[j]:
      ind2=[j, mat[j].index(i[1])]
  if ind1[0] == ind2[0]:
    ct.append(mat[ind1[0]][(ind1[1]+1)%6] + mat[ind2[0]][(ind2[1]+1)%6])
  elif ind1[1] == ind2[1]:
    ct.append(mat[(ind1[0]+1)%6][ind1[1]] + mat[(ind2[0]+1)%6][ind2[1]])
  else:
    ct.append(mat[ind1[0]][ind2[1]] + mat[ind2[0]][ind1[1]])
print(''.join(ct))