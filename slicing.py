import numpy as np

array=np.array([2,56,7,89,64,33,2,3])
print("Slicing    ")
print(array[1:4])
print(array[:5])
print(array[::2])
print(array[::-1])
print(array[0:5:2])


print("Fancy indexing")

print(array[[0,3,6]])


print("Boolen masking")

print(array[array>20])
print(array[(array < 20) | (array > 60)])