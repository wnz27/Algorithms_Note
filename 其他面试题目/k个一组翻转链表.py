'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-14 18:39:00
@LastEditTime: 2020-03-14 23:38:51
@FilePath: /Algorithms_Note/其他面试题目/k个一组翻转链表.py
@description: type some description
'''
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 递归方法
    def reverseKGroup1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        curr = head
        pre = None
        for i in range(k - 1):
            if curr == None:
                break
            curr = curr.next
        if curr == None:
            return head
        else:
            curr = head
            for i in range(k):
                tem = curr.next
                curr.next = pre
                pre = curr
                curr = tem
            head.next = self.reverseKGroup(curr, k)
        return pre
    # 使用栈
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        p = dummyhead
        while True:
            count = k
            s = []
            tmp = head
            while count and tmp:
                s.append(tmp)
                tmp = tmp.next
                count -= 1
            if count:   # 也就是上面终止循环的条件是tmp变空了，但是还不够k个，所以直接跳出主循环
                p.next = head
                break
            # 否则就是因为count=0退出的上面循环，那么现在tmp停在了k+1的位置
            while s:
                p.next = s.pop()
                p = p.next
            # 连接剩下的链表
            p.next = tmp
            head = tmp
        return dummyhead.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
# l4.next = l5
s = Solution()
print(s.reverseKGroup(l1, 3).val)
        