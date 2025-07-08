import numpy as np

array =np.array([2,3,4,5,6,7,8,86,5])
print("Reshape")
print(array.reshape(3,3))
print(array)

print("Flattening array")

array1=np.array([[1,45,66,7],[3,4,6,8]])
print(array1)
print(array1.ravel())
print(array1)
print(array1.flatten())