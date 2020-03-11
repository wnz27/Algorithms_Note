'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-11 18:18:21
@LastEditTime: 2020-03-11 20:57:24
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/复制复杂链表.py
@description: type some description
'''
'''
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 
指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
示例1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node_index = {}  # {node:index}
        tem = head
        n = 0
        while tem:
            node_index.setdefault(tem, n)
            tem = tem.next
            n += 1
        origin_head = head
        dummy_head = Node(0)
        p = dummy_head
        random_helper = {}  # 用来保存还未建立连接的random的节点,{index:random}
        for i in range(n):      # 先建立索引
            random_helper[i] = Node(origin_head.val)
            p.next = random_helper[i]
            p = p.next
            origin_head = origin_head.next
        origin_head = head
        p = dummy_head
        for i in range(n):      # 匹配random
            if origin_head.random == None:
                random_helper[i].random = None
            else:
                random_index = node_index[origin_head.random]
                random_helper[i].random = random_helper[random_index]
            p = p.next
            origin_head = origin_head.next
        return dummy_head.next
            