'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-12 10:47:18
@LastEditTime: 2020-03-12 11:02:17
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/15从上打印二叉树I.py
@description: type some description
'''
'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        q = []
        q.append(root)
        while q:
            tem = q.pop(0)
            if tem != None:
                res.append(tem.val)
                q.append(tem.left)
                q.append(tem.right)
            else:
                continue
        return res
