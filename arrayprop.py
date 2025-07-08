import numpy as np 

array=np.array([[23,4,5,6,7],[4,5,6,4,5]])
print(array)
print("Shape of array ")
print(array.shape)
print("size of array")
print(array.size)
print("Number of dimensions")
print(array.ndim)

print("Type of array")
print(array.dtype)

array1=np.array([2.3,4.5,6.7,8.9])
print(array1.astype(int))
print("Change type of array")
print(array1)