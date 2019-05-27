# -*- coding:utf-8 -*-

#QUESTION DESCRIPTION
'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.

'''

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        def delRepeatAndSort (lst):
            '''
            把列表去重和排序
            '''

            #方法一32ms
            '''
            sortList = sorted(lst)
            delRepeatAndSortedList = []
            for i in sortList:
                if i not in delRepeatAndSortedList:
                    delRepeatAndSortedList.append(i)
            return delRepeatAndSortedList
            '''

            #方法二32ms
            return list(set(lst))

        def findJFromS(jList,sList):
            '''
            从S里挑出J
            '''
            j_variety = 0                                               #最终珠宝个数
            for index in range(len(jList)):                             #遍历不同种类珠宝数，然后从s中找出每种个数相加即可
                for jewel in sList:
                    if jewel == jList[index]:
                        j_variety += 1
                        continue
                    else:
                        continue
            return j_variety

        j_list = list(J)
        s_list = list(S)                                             #字符串变成字母字符的列表
        j_orderd_list = delRepeatAndSort(j_list)
        j_variety = findJFromS(j_orderd_list,s_list)
        return j_variety

       
        

cs = Solution()

v = "aaaaAAAAAA"

n = "aAAbaaabbAAAAbbb"

print(cs.numJewelsInStones(v,n))

