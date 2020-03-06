'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-05 01:21:56
@LastEditTime: 2020-03-05 01:24:38
@FilePath: /Algorithms_Note/algorithms_practice/合并排序链表.py
@description: type some description
'''
'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(1)
        p = dummyHead
        h1 = l1
        h2 = l2
        while h1 != None and h2 != None:
            if h1.val <= h2.val:
                p.next = ListNode(h1.val)
                h1 = h1.next
            else:
                p.next = ListNode(h2.val)
                h2 = h2.next
            p = p.next
        if h1 == None:  # h2 != None
            p.next = h2
        else:  # h2 == None h1 != None
            p.next = h1
        return dummyHead.next
