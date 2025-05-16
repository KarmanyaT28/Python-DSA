import numpy as np


twoDArray = np.array([[11,22,33,44],[12,24,36,48],[10,20,30,40],[100,200,300,400]])
print(twoDArray)



def accessElement(array,rowIndex,colIndex):
    if rowIndex >=len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')

    else:
        print(array[rowIndex][colIndex])


accessElement(twoDArray,2,3)





# Time Complexity : O(1)
# Space Complexity : O(1)
