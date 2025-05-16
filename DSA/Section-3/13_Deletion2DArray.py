import numpy as np



twoDArray = np.array([[11,22,33,44],[12,24,36,48],[10,20,30,40],[100,200,300,400]])
print(twoDArray)



newTDArray = np.delete(twoDArray,1,axis=1)

print(newTDArray)



# Time Complexity : O(mn)
# Space Complexity : O(mn)



# axis = 0 operates for row
# axis = 1 operates for column