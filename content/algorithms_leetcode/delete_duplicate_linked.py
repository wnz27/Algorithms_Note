# -*- coding:utf-8 -*-
# @UpdateTime : 2021/3/26 12:18 下午
# @Author : a27
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。
示例 1：
输入：head = [1,1,2]
输出：[1,2]
示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def delete_duplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        dumy_head = None
        p = head

        duplicate = {}

        while p:
            curr_value = p.val
            if curr_value in duplicate:
                # 删除当前节点
                dumy_head.next = p.next
                p = p.next
            else:
                # 把值放进去
                duplicate[curr_value] = 1

                # 往后移动指针
                dumy_head = p
                p = p.next
        return head


if __name__ == '__main__':
    pass
