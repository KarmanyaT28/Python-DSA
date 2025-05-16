from array import *


arr1 = array('i',[1,2,3,4,5,6,7,8,9])


def LinearSearch(array,target):

    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1


print(LinearSearch(arr1,8))



# Time Complexity : O(N)
# Space Complexity : O(1)
