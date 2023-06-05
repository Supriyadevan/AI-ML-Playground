import numpy as np
arr = np.array([1,2,3])
arr11 = np.array(range(3))
arr12 = np.array([4,5,6])
array2D = np.array([arr11, arr12])
array2D1 = np.array([[7,8,9], [10,11,12]])
array3D = np.array([array2D, array2D1])
print("arr11 is ... ",arr11.ndim, arr11.size,arr11.shape, arr11)
print("O-D Array of 42 ...",np.array(42).ndim, np.array(42).shape, np.array(42))
print("array2D....",array2D.ndim,array2D.size,array2D.shape, array2D)
print("array3D....",array3D.ndim, array3D.size, array3D.shape, array3D)

arrnDim = np.array(range(10), ndmin=5)
print("Crazy Array...", arrnDim)

for x in arr:
    print(x)
print(arr)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr1:
    print(x)

arr2 = np.array([[[[[1,2,3]]]]])
for x in arr2:
    print(x)

#concatenate
arr3 = np.array([[1,2,3],[11,22,33]])
arr4 = np.array([[4,5,6],[44,55,66]])

arr5 = np.concatenate((arr3,arr4),axis=1)
print(arr5)

arr6 = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr6 == 4)

print(x)

z = np.array([1,3,4,5,6,9])
y = np.searchsorted(z,7)
print(y)

