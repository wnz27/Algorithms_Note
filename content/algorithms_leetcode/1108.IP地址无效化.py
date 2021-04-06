'''
@Author: 27
@LastEditors: 27
@Date: 2019-10-29 17:34:27
@LastEditTime: 2020-03-03 08:25:46
@FilePath: /Algorithms_Note/algorithms_practice/1108.IP地址无效化.py
@description: type some description
'''
'''
给你一个有效的 IPv4 地址address，返回这个 IP 地址的无效化版本。

所谓无效化IP 地址，其实就是用"[.]"代替了每个 "."。

示例 1：

输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"
示例 2：

输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"

提示：
给出的 address 是一个有效的 IPv4 地址

'''
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ''
        for everyChar in address:
            if everyChar == '.':
                result += '[.]'
            else:
                result += everyChar
        return result
    def defangIPaddr2(self, address):
        """
        :type address: str
        :rtype: str
        """
        return '[.]'.join(address.split('.'))

