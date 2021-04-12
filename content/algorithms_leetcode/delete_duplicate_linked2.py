# -*- coding:utf-8 -*-
# @UpdateTime : 2021/3/26 12:18 下午
# @Author : a27

"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。
返回同样按升序排列的结果链表。
示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]
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

        duplicate = {}
        p = head
        dumy_head = None
        while p:
            curr_value = p.val
            if curr_value in duplicate:
                duplicate[curr_value] += 1
            else:
                duplicate[curr_value] = 1
            p = p.next
        p = head
        while p:
            curr_value = p.val
            curr_value_count = duplicate[curr_value]
            if curr_value_count > 1:
                # 断操作
                # 开头的边界情况要判断一下
                if dumy_head:
                    dumy_head.next = p.next
                    p = p.next
                else:
                    head = p.next
                    p = head
            else:
                dumy_head = p
                p = p.next
        return head


if __name__ == '__main__':
    pass


