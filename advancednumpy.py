import numpy as np

array1=np.array([1,3,4,6])
print("Insertion")
new_arr=np.insert(array1,3,9)
print(new_arr)
array_2d=np.array([[2,4,3,2],[6,87,54,3]])
arr2d_new=np.insert(array_2d,2,0,axis=0)
print("Insertion 2d")
print(arr2d_new)

array2=np.array([34,5,6,7])
print("concatenate , join of the array")
array_new=np.concatenate((array1,array2))
print(array_new)
array1_reshape=array1.reshape(2,2)
array2_reshape=array2.reshape(2,2)
array3=np.concatenate((array1_reshape,array2_reshape),axis=1)
print("2d_array")
print(array3)

print("Vstack")
arraynew=np.vstack((array1,array2))
print(arraynew)

print("split")
arraysplit=np.hsplit(array1_reshape,2)
print(arraysplit)


