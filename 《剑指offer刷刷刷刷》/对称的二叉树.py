'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-11 12:37:00
@LastEditTime: 2020-03-11 16:09:08
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/对称的二叉树.py
@description: type some description
'''
'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.helper(root.left, root.right)
        
    def helper(self, leftnode, rightnode):
        if leftnode == None and rightnode == None:
            return True
        if leftnode == None or rightnode == None:
            return False
        if leftnode.val != rightnode.val:
            return False
        return self.helper(leftnode.left, rightnode.right) and self.helper(leftnode.right, rightnode.left)         
    # 迭代
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        # 借助队列，这里需要广度优先
        que = []
        que.append(root.left)
        que.append(root.right)
        while len(que) != 0:
            l = que.pop(0)
            r = que.pop(0)
            if l == None and r == None:
                continue        # 细节是魔鬼哎！！！！！！
            if l == None or r == None:
                return False
            if l.val != r.val:
                return False
            que.append(l.left)
            que.append(r.right)
            que.append(l.right)
            que.append(r.left)
        return True
        
        
        
        