#! -*- coding=utf-8 -*-
'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        head = prev
        return head

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        next_n_node = None
        m_node = head
        prev_m_node = None
        count = 1
        cur = head
        prev = None
        while count < n:
            if count == m:
                m_node = cur
                prev_m_node = prev
            prev = cur
            cur = cur.next
            count += 1
        next_n_node = cur.next  # 保留住原始链表的n的下一个节点
        cur.next = None  # 把第n个节点的next置空
        n_node = self.reverseList(m_node)
        # 拼接链表把第m-1个节点的next指向n，第m个节点指向最初n节点的下一个节点
        if prev_m_node:
            prev_m_node.next = n_node
            m_node.next = next_n_node
            return head
        else:
            m_node.next = next_n_node
            return n_node
        
        






            
