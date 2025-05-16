from array import *

arr1 = array('i',[1,2,3,4,5])


def accessElement(array,index):
    if index > len(array):
        print("There is no element at this index")
    else:
        print(array[index])


accessElement(arr1,4)

accessElement(arr1,3)

accessElement(arr1,7)


# Time Complexity : O(1)

# Space Complexity : O(1)