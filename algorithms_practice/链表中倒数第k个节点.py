'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-04 16:42:06
@LastEditTime: 2020-03-04 16:49:57
@FilePath: /Algorithms_Note/algorithms_practice/链表中倒数第k个节点.py
@description: type some description
'''
'''
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，
即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.

'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "{}".format(self.val)

class Solution(object):
    # 迭代版
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        target = k
        count = 0
        p, q = head, head
        while p != None:
            p = p.next
            if count >= target:
                q = q.next
            count += 1
        return q
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
s = Solution()
print(s.getKthFromEnd(l1,2))
