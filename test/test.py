'''
@Author: 27
@LastEditors: 27
@Date: 2020-02-25 12:04:45
@LastEditTime: 2020-03-10 10:35:18
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

print("*"*80)

print(list("11223"))
print(int('0'), int('1'))
print(('10001000'+'1')[::-1])

def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        m = nums[i]
        if (target - m) in dict:
            return (dict[target - m], i)
        else:
            dict[m] = i

print(twoSum([5,7,3,10,4], 11))
print("2", 10 * ' ', "2")

len_1 = min(['12','244','3555','46'], key=lambda x: len(x))
print(len_1)


print([1,2,3].pop())
print('adf adfa adf '.split())
a = {}
a.setdefault(1, 'nont')
a.setdefault(1, 'aaaaa')
print(a)

a = [1,0,5]
a.sort()
print(a)

for i in {1:2, 5:6}:
    print(i)

print("*".join("adfa adsff asdf ".split()))
import collections
a = collections.defaultdict(int)
print(a)
print(max(a['123'], 2))
print("*" * 80)
b = {1:10,2:30}
key = max(b , key= lambda x: [x])
print(key, b[key])

print([2,1,1,2][1::2])
print([2,1,1,2][:4:2])

print([2] * 10)
print([] + ["123"])
print(["123"] + ["666"])

a = [1,1,1,1,0,0,5]
print(max(a))

      

a = [(0,5), (6,7)]
print(max(a, key=lambda x: x[1]-x[0]))


print([1,3][1:2])

print(sum([1,2,3,4][:2]))

a = [1,10]
a.insert(len(a), 90)
print(a)
a.reverse()
print(a)

def test(a, b=10):
    print(a, b)

test(99999)
test(888,28)

print('.' in 'adfadf.adfafaf')
print('adf.rqewr.145234'.split('.'))
q = collections.deque()
q.append(1)
q.append(2)
print(q)

print([0]*4)

a = [1,23,4]
for i in a:
    i += 1  # 迭代里的i，调用不到list的set方法
    print(a)

print(int(9/2))


line = [i for i in range(1,9+1)]
print(line)

print(list(range(1,10)))
print(line[6:11])
print(sum(line[9:11]))
print(sum([]))
for i in range(10,9, -1):
    print(i)
print([None] * 10)

# [].pop()
print(9//5)
print(9//10)
a = [1,2,3,4]
print(a[:1] + a[1+1:])
print(list(range(10+1)[:0:-1]))
a = {1:99}
a[27] = 80
a[3] = 100
print(a)
print(1 in a)
print(float('inf') + 1)

print(-~1)
print(~-2)
a = 1
b = 2
a^=b
b^=a
a^=b
print(a, b)
print("*" * 80)
b = {1:10,2:30}
key = max(b , key= lambda x: x<20)
print(key, b[key])

print(int('1'))
print('2'.isdigit())
print(9//10)
a = 1
if a == 1:
    print('77777',a)
elif a<10:
    print("123123123122dsafasf")

for k,v in {1:23, 4:56}.items():
    print(k, v)
b.setdefault(3, None)
b.setdefault(1, 7)
print(b)
def findRepeatNumber(nums):
        import random
        """
        :type nums: List[int]
        :rtype: int
        """
        helper = {}
        res = []
        # 哈希
        for i in nums:
            if i in helper:
                helper[i] += 1
            helper.setdefault(i, 1)
        for k,v in helper.items():
            if v > 1:
                res.append(k)
        print(helper, res)
        if res != []:
            random.shuffle(res)
            return res[0]
        else:
            return -1
findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
# print(len([][0]))IndexError: list index out of range
a= []
print(not a)