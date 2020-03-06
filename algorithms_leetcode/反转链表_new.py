'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-02 02:30:53
@LastEditTime: 2020-03-02 03:21:57
@FilePath: /Algorithms_Note/algorithms_practice/反转链表_new.py
@description: type some description
'''
'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "{}".format(self.val)

# 方法一 迭代
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        curr = head
        while curr:
            tem = curr.next
            curr.next = pre
            pre = curr
            curr = tem
        return pre

# 方法二 递归
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
         # 递归
        pre = None
        curr = head
        return self.helper(pre, curr)
    def helper(self, pre, curr):
        if curr.next == None:  # base：如果下一个节点为空，则到最后了，直接把最后一个节点指向前一个，然后返回最后一个节点
            curr.next = pre
            print(curr)  # 这里可以打印出值为什么返回的是空？
            return curr
        else:  # 不是最后一个节点
            tem = curr.next  # 保存下来下一个节点
            curr.next = pre  # 翻转
            pre = curr       # 把前一个指针指向当前
            curr = tem       # 把当前节点往后移动
        self.helper(pre, curr)
s = Solution2()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
print(s.reverseList(l1))