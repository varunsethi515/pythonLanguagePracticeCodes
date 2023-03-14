from numpy import *
matrix1=matrix('1,2,3; 4,5,6; 7,8,9')
matrix2=matrix('9,8,7; 6,5,4; 3,2,1')
matrix3=matrix('0,0,0; 0,0,0; 0,0,0')
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
for r in range(matrix3):
    print(matrix3)
