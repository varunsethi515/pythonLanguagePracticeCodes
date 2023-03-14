from numpy import *
array1=array([1,2,3,4,5])
print(array1)
print(array1.dtype)
print(array1.ndim)
print(array1.shape)
print(array1.size)
array2=array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
print(array2)
print(array2.dtype) # it will return the data type of the array
print(array2.ndim) # it will return the dimension of the array
print(array2.shape) # it will return the number of rows and number of columns
print(array2.size) # it will return the product of no of rows and number of columns
array3=array2.flatten() # it will convert the given matrix into 1D
print(array3)
array4=array3.reshape(3,4) # it will convert 1D matrix into Multi Dimension
print(array4)

# Matrix
matrix1=matrix(array2)
print(matrix1)
print(diagonal(matrix1))
print(matrix1.min())
print(matrix1.max())
matrix2=matrix('1,2,3; 4,5,6; 7,8,9')
print(matrix2)
matrix3=matrix('9,8,7; 6,5,4; 3,2,1')
print(matrix3)
print(matrix2 * matrix3) # in python with the help of matrix method you can simplify multiply two matrix using ' * '



