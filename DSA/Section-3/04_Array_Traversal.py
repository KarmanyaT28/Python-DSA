from array import *

arr1 = array('i',[1,2,3,4,5,6,7,8,9])

arr2 = array('d',[1.3,3.4,6.8])

print(arr1)

arr1.insert(2,9)

print(arr2)


def traverseArray(array):
    for i in array:
        print(i)



traverseArray(arr1)


# Time Complexity : O(N)
# Space Complexity : O(1)

