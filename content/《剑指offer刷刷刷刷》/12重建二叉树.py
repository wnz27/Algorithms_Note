'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-11 08:58:42
@LastEditTime: 2020-03-11 10:52:12
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/重建二叉树.py
@description: type some description
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        curr_root_val = preorder[0]
        curr_root_index_in_inorder = inorder.index(curr_root_val)
        rootNode = TreeNode(curr_root_val)
        left_tree_pre = preorder[1:1+curr_root_index_in_inorder]
        left_tree_in = inorder[:curr_root_index_in_inorder]
        right_tree_pre = preorder[1+curr_root_index_in_inorder:]
        right_tree_in = inorder[1+curr_root_index_in_inorder:]
        rootNode.left = self.buildTree(left_tree_pre, left_tree_in)
        rootNode.right = self.buildTree(right_tree_pre, right_tree_in)
        return rootNode
    
s = Solution()
a = s.buildTree([3,9,20,15,7],[9,3,15,20,7])
print(a)