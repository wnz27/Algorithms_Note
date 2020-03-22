'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-12 10:56:37
@LastEditTime: 2020-03-12 13:12:42
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/17从上到下打印二叉树III.py
@description: type some description
'''
'''
请实现一个函数按照之字形顺序打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，
第三行再按照从左到右的顺序打印，其他行以此类推。

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
  [20,9],
  [15,7]
]
提示：
节点总数 <= 1000
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 方法一、双栈
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q1, q2 = [], []
        res = []
        q1.append(root)
        level = 1
        while q1 or q2:
            line = []
            if level % 2 != 0:  # 单数行从q1往外弹数据
                while q1:
                    tem = q1.pop()
                    if tem != None:     # 下一行要从右向左，先把左入栈
                        q2.append(tem.left)
                        q2.append(tem.right)
                        line.append(tem.val)
                    else:
                        continue
                if line:
                    res.append(line)
                level += 1
            else:   #偶数行从q2往外弹数据
                while q2:
                    tem = q2.pop()
                    if tem != None:     # 下一行要从左向右，先把右入栈
                        q1.append(tem.right)
                        q1.append(tem.left)
                        line.append(tem.val)
                    else:
                        continue
                if line:
                    res.append(line)
                level += 1
        return res
    
    # 方法二、双端队列
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        import collections
        q = collections.deque()
        res = []
        q.append(root)
        level = 1
        while q:
            line = []
            if level % 2 != 0:  # 单数行用pop出队，用appendleft入队，先左再右
                n = len(q)
                for _ in range(n):  # 遍历当前行
                    tem = q.pop()
                    if tem != None:
                        line.append(tem.val)
                        q.appendleft(tem.left)  # 下一行要从右到左，先把左入队
                        q.appendleft(tem.right)
                    else:
                        continue
                if line:
                    res.append(line)
                level += 1
            else:               # 双数行用popleft出队，用append入队，先右再左
                n = len(q)
                for _ in range(n):  # 遍历当前行
                    tem = q.popleft()
                    if tem != None:
                        line.append(tem.val)
                        q.append(tem.right)
                        q.append(tem.left)
                    else:
                        continue
                if line:
                    res.append(line)
                level += 1
        return res
    def levelOrder3(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 单队列双百分百！！！！
        if not root:
            return []
        q = []
        res = []
        q.append(root)
        while q:
            line = []
            n = len(q)
            for _ in range(n):
                tem = q.pop(0)
                if tem != None:
                    line.append(tem.val)
                    q.append(tem.left)
                    q.append(tem.right)
                else:
                    continue
            if line:
                res.append(line[::-1] if len(res) % 2 else line)
        return res
            