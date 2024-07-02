#multipilcation of 2 matrices
#for matrix 1 reading data
rows1=int(input("Enter the no.of rows for matrix 1:"))
cols1=int(input("Enter the no.of column for matrix 1:"))
matrix1=[]
print("Enter the matrix1 elements:")
for row in range(0,rows1):
    rows=[]
    for col in range(0,cols1):
        x=int(input())
        rows.append(x)
    matrix1.append(rows)


#for matrix 2 reading data
rows2=int(input("Enter the no.of rows for matrix 2:"))
cols2=int(input("Enter the no.of column for matrix 2:"))
matrix2=[]
print("Enter the matrix1 elements:")
for row in range(0,rows2):
    rows=[]
    for col in range(0,cols2):
        x=int(input())
        rows.append(x)
    matrix2.append(rows)

matrix3=[]
for row in range(rows1):
    rows=[]
    for col in range(cols2):
        rows.append(0)
    matrix3.append(rows)
if cols1!=rows2:
    print("Multiplication is not possible!!")
else:
#multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(rows2):
                matrix3[i][j]=matrix1[i][k]*matrix2[k][j]

for i in matrix3:
    print(i)