import numpy as np

array=np.array([1,2,np.nan,4,5])
print(np.isnan(array))

print(np.nan_to_num(array,nan=100))

array2=np.array([3,4,67,8,np.inf,-np.inf])
print(np.isinf(array2))
print(np.nan_to_num(array2,posinf=23,neginf=45))

print("sort")
print(np.sort(array))

