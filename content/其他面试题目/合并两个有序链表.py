'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 09:42:41
@LastEditTime: 2020-05-02 00:09:11
@FilePath: /Algorithms_Note/content/其他面试题目/合并两个有序链表.py
@description: type some description
'''
'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 开辟额外空间
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q = l1, l2
        dummyhead = ListNode(0)
        curr = dummyhead
        while p or q:
            v1 = p.val if p != None else float("inf")
            v2 = q.val if q != None else float("inf")
            if v1 <= v2:
                curr.next = ListNode(v1)
                curr = curr.next
                p = p.next
            else:
                curr.next = ListNode(v2)
                curr = curr.next
                q = q.next
        return dummyhead.next

    # 不开辟额外空间
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        dummy = pre
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 if l1 else l2
        return pre.next

    # 递归
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l2.next, l1)
            return l2

    # 利用数组
    def mergeTwoLists3(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        tmp = []
        while l1 and l2:
            if l1.val < l2.val:
                tmp.append(l1)
                l1 = l1.next
            else:
                tmp.append(l2)
                l2 = l2.next
        if l1 is None:
            while l2:
                tmp.append(l2)
                l2 = l2.next
        else:
            while l1:
                tmp.append(l1)
                l1 = l1.next
        for i in range(len(tmp) - 1):
            tmp[i].next = tmp[i + 1]
        return tmp[0] if len(tmp) > 0 else None
