'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 08:21:36
@LastEditTime: 2020-03-14 08:46:25
@FilePath: /Algorithms_Note/其他面试题目/有效的括号.py
@description: type some description
'''
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        helper = {")": "(", "}":"{", "]": "["}
        base = 0
        st = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                st.append(char)
                base += 1
            if char in helper:
                if not st:
                    return False
                else:
                    if helper[char] == st[-1]:
                        st.pop()
                        base -= 1
                    else:
                        return False
        return base == 0
s = Solution()
print(s.isValid(")("))