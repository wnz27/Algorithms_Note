'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-23 19:31:27
@LastEditTime: 2020-03-23 19:31:51
@FilePath: /Algorithms_Note/content/其他面试题目/链表的中间节点.py
@description: type some description
'''
'''
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
示例 1：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        helper = []
        while curr:
            helper.append(curr)
            curr = curr.next
        helper_length = len(helper)
        if helper_length == 0:
            return None
        return helper[int(helper_length / 2)]
