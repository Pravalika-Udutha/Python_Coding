#addition of 2 matrices

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

#addition of matrices
matrix3=[]
for row in range(rows1):
    rows=[]
    for col in range(cols1):
        rows.append(matrix1[row][col]+matrix1[row][col])
    matrix3.append(rows)
for row in matrix3:
    print(row)