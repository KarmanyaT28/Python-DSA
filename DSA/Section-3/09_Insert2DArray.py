# Printing 2d Array



# Day 1 - 11,32,76
# Day 2 - 12,45,23
# Day 3 - 71,63,22
# Day 4 - 15,18,4


import numpy as np

twoDArray= np.array([[11,32,76],[12,45,23],[71,63,22]])


print(twoDArray)



newtwoDArray = np.insert(twoDArray,0,[[1,2,3]],axis=1)
print(newtwoDArray)


newtwoDArray = np.insert(twoDArray,1,[[1,2,3]],axis=0)
print(newtwoDArray)


newtwoDArray = np.append(twoDArray, [[1,2,3]] , axis=0)
print(newtwoDArray)


# Time Complexity : O(mn)
# Space Complexity : O(mn)
