'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-11 18:14:37
@LastEditTime: 2020-03-12 00:00:16
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/删除链表节点.py
@description: type some description
'''
'''
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
注意：此题对比原题有改动

示例 1:
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
'''
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return -1
        dummyhead = ListNode(0)
        dummyhead.next = head
        p = dummyhead
        q = head
        while q != None:
            if q.val == val:
                break
            p = p.next
            q = q.next
        if q == None:       # 处理没进入循环的情况，即不存在删除目标
            return head
        else:
            if q.next == None:  # 被删节点是最后一个
                p.next = None
            else:               # 普遍情况
                p.next = q.next
        return dummyhead.next
