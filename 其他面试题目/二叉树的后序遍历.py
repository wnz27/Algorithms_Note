'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-17 16:24:19
@LastEditTime: 2020-03-17 20:06:32
@FilePath: /Algorithms_Note/其他面试题目/二叉树的后序遍历.py
@description: type some description
'''
'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 递归方法
    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if not root:
            return 
        if root.left:
            self.helper(root.left, res)
        if root.right:
            self.helper(root.right, res)
        res.append(root.val)

    # 非递归
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """    
        if not root:
                return []
        pops = []   # 深度栈
        s = []      # 最终顺序栈
        pops.append(root)
        while pops:
            tem = pops.pop()
            s.append(tem.val)
            if tem.left:
                pops.append(tem.left)
            if tem.right:
                pops.append(tem.right)
        return s[::-1]
        
    
