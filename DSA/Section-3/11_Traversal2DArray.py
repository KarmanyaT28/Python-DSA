import numpy as np


twoDArray = np.array([[11,22,33,44],[12,24,36,48],[10,20,30,40],[100,200,300,400]])
print(twoDArray)



def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverse2DArray(twoDArray)




# Time Complexity : O(n^2)
# Space Complexity : O(1)
