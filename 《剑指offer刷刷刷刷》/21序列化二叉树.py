'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-13 17:29:15
@LastEditTime: 2020-03-13 20:24:42
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/21序列化二叉树.py
@description: type some description
'''
'''
请实现两个函数，分别用来序列化和反序列化二叉树。
示例: 
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Codec:
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return "[]"
#         q = []
#         q.append(root)
#         tmp = []
#         # 先把节点按层加入
#         while q:
#             l = len(q)
#             line = []
#             for _ in range(l):
#                 tem = q.pop(0)
#                 if tem != None:
#                     line.append(str(tem.val))
#                     q.append(tem.left)
#                     q.append(tem.right)
#                 else:
#                     line.append("null")
#             tmp.append(line)
#         tmp.pop()
#         res = "["
#         for level in tmp:
#             for i in level:
#                 res += i + ","
#         return res[:-1] + "]"

        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data:
#             return []
#         handle_data = data.strip('[]').split(',')
#         res = []
#         level = []
#         standard = 1
#         count = 0
#         for i in handle_data:
#             if count == standard:
#                 count = 0
#                 standard *= 2
#                 res.append(level)
#                 level = []
#             if i == "null":
#                 level.append(None)
#             else:
#                 newNode = TreeNode(int(i))
#                 level.append(newNode)
#             count += 1
#         res.append(level)
#         print(res)
#         for level in range(len(res) - 1):
#             for i in range(len(res[level])):
#                 if res[level][i]:
#                     res[level][i].left = res[level + 1][i * 2]
#                     res[level][i].right = res[level + 1][i * 2 + 1]
#         return res[0][0]
                
# s = Codec()
# a = s.deserialize("[1,2,3,null,null,4,5]")
# print(a.val, a.left.val, a.right.val, a.right.left.val, a.right.right.val)
# print(s.serialize(a))
            
            
                
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))