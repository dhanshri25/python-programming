from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([2,3,4,5,6])

arr = arr1 + arr2
print(arr)

print(concatenate([arr1,arr2]))

arr3 = arr1.copy()

print(arr3)