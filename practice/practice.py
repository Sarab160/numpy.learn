import numpy as np
import numpy as np

A = np.array([
    [12,  5,  7, 10],
    [ 3, 15, 11,  2],
    [19,  4,  8, 14],
    [ 6, 13,  1, 16]
])
print("Detail about matrix.")
print(A)
print(A.ndim)
print(A.shape)
print("Make new matrix 2D ith default values.")
B=np.full((4,4),2)
print(B)
print("Sum of two matrix.")
new_matrix=A+B
print(new_matrix)
print("Make sinlge matrix with arrange function.")

array=np.arange(0,100,1)
print("Size of array")
print(array)
print(new_matrix.size)
print("Mean of sd array")
print(new_matrix.mean())

print("slicing")

print(new_matrix[0:3,2:3])

print(new_matrix[0:3,2])
print(new_matrix[0:2,:])
print(new_matrix[:,0:1])
print(new_matrix[::2,0:1])
print(array[0:3])
print("Print boolen massing")

cond=array[(array>50)&(array%2==0)]
print(cond)

column_condition=np.all(new_matrix>10,axis=1)
print(column_condition)

print(array.reshape(5,20))

print(np.where(new_matrix==21))