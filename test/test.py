'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-25 12:04:45
@LastEditTime: 2020-02-26 01:52:54
@FilePath: /Algorithms_Note/test/test.py
@description: type some description
'''
print(sum([1,2,3]))
print(list(range(1,1)))
print(sum([]))

print([1,2,3] + [4,6])
print([1,2,3,4].index(max([1,2,3,4])))

def dominantIndex(nums):
        maxi = max(nums)
        max_index = nums.index(maxi)
        if all(maxi >= 2*x for x in nums if x != maxi):
            return max_index
        return -1
print(dominantIndex([1,1,1,1]))


for i in range(10)[::-1]:
    print(i)

a , b = 1, 10
print(a, b)
print("*"*80)
print(not [[],[],[]])
b = [1,2]
b.extend([11])
print(b)
column = 1
row = 9
N = 10
print("*"*80)
column += (row == N - 1)
print(column)
def findDiagonalOrder(matrix):
    
    # Check for empty matrices
    if not matrix or not matrix[0]:
        return []
    
    # Variables to track the size of the matrix
    N, M = len(matrix), len(matrix[0])
    
    # The two arrays as explained in the algorithm
    result, intermediate = [], []
    
    # We have to go over all the elements in the first
    # row and the last column to cover all possible diagonals
    for d in range(N + M - 1):
        
        # Clear the intermediate array everytime we start
        # to process another diagonal
        intermediate.clear()
        
        # We need to figure out the "head" of this diagonal
        # The elements in the first row and the last column
        # are the respective heads.
        r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
        
        # Iterate until one of the indices goes out of scope
        # Take note of the index math to go down the diagonal
        while r < N and c > -1:
            intermediate.append(matrix[r][c])
            r += 1
            c -= 1
        
        # Reverse even numbered diagonals. The
        # article says we have to reverse odd 
        # numbered articles but here, the numbering
        # is starting from 0 :P
        if d % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)
    return result        

