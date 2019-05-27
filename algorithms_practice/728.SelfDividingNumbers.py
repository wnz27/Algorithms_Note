# -*- coding:utf-8 -*-

#QUESTION DESCRIPTION
'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, 
including the bounds if possible.

Example 1:

Input: 
left = 1, right = 22

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

'''
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right+1):
            if self.isAllZero(i):
                result.append(i)
            else:
                continue     
        return result

              
    
    def isAllZero(self,num):
        '''
        传入任意一个数，拿到它每一位上的数字,然后用这个数除以它每一位的数字，
        如果余数全部为零，返回true，否则返回false
        '''
        try:
            for digit in str(num):
                if num%int(digit)==0:
                    continue
                else:
                    return False
            return True
        except:
            return False