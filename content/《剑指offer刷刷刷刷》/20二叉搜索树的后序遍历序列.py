'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-13 16:43:40
@LastEditTime: 2020-03-13 17:27:55
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/20二叉搜索树的后序遍历序列.py
@description: type some description
'''
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false
示例 2：
输入: [1,3,2,6,5]
输出: true
'''
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        '''
        每个节点大于左子树小于右子树
        '''
        if len(postorder) > 3:

    def judgePostorderAvl(self, l):
        if len(l) <= 2:
            return True
        elif len(l) == 3:
            return True if l[1] > l[2] > l[0] else False
        else:
            
