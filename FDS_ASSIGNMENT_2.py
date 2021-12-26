r,c =[int(x) for x in input("Enter Size:").split()]

m1=[]
for i in range(r):
  print("Row-:",i+1,end='')
  a=[int(x) for x in input().split()]
  m1.append(a)

m2=[]
for i in range(r):
  print("Row-:",i+1,end='')
  a=[int(x) for x in input().split()]
  m2.append(a)

addition_matrix=[]
for i in range(r):
  z=[]
  for j in range(c):
    z.append(m1[i][j]+m2[i][j])
  addition_matrix.append(z)

subtraction_matrix=[]
for i in range(r):
  z=[]
  for j in range(c):
    z.append(m1[i][j]-m2[i][j])
  subtraction_matrix.append(z)

print("Addition of Matrix:",addition_matrix)
print("Subtraction of Matrix:",subtraction_matrix)

multiplication_matrix=[[0 for j in range(c)]for i in range(3)]
for i in range(r):
  for j in range (r):
    for k in range(r):
      multiplication_matrix[i][j]=multiplication_matrix[i][j]+m1[i][k]*m2[k][j]
print("Multiplication of Matrix:",multiplication_matrix)

transpose_1=[]
for i in range(c):
  for j in range(r):
    p=m1[j][i]
    transpose_1.append(p);
print("Transpose of Matrix 1:",transpose_1)

transpose_2=[]
for i in range(c):
  for j in range(r):
    q=m2[j][i]
    transpose_2.append(q);
print("Transpose of Matrix 2:",transpose_2)
