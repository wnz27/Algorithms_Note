'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-05 09:32:36
@LastEditTime: 2020-03-05 09:33:26
@FilePath: /Algorithms_Note/algorithms_practice/从上到下打印二叉树II.py
@description: type some description
'''
'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        s = []
        res = []
        s.append(root)
        while s != []:
            l = len(s)
            line = []
            for _ in range(l):  # 按行处理
                tem = s.pop(0)
                if tem != None:
                    line.append(tem.val)
                    s.append(tem.left)
                    s.append(tem.right)
                else:
                    continue
            if line != []:
                res.append(line)
        return res
