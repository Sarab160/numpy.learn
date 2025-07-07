import numpy as np

array =np.array([1,2,3,4,5,6])
print("simple array in numpy ")

print(array)

array2d=np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print("2D Array: ")
print(array2d)

print("Mean: ")
print(np.mean(array))

print("Default values: ")

default=np.zeros(3)
def1=np.ones((2,2))
def2=np.full((2,3),6)

print(default)
print(def1)
print(def2)

print("Arrange the value that start form one point go to other point and take step: ")

arr=np.arange(1,60,3)

print(arr)

print("Identity Matrix: ")
identity=np.eye(4)

print(identity)


