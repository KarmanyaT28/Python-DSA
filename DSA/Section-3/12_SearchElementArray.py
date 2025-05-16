import numpy as np


twoDArray = np.array([[11,22,33,44],[12,24,36,48],[10,20,30,40],[100,200,300,400]])
print(twoDArray)



def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index '+str(i)+" "+str(j)
            
    return 'The element is not found'


print(searchTDArray(twoDArray,44))



# Time Complexity : O(mn)
# Space Complexity : O(1)
