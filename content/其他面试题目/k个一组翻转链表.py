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

        # 先看这组待翻转够不够k个
        for i in range(k - 1):  # k-1原因是这样执行curr = curr.next之后，curr会停在第k个节点上
            if curr is None:
                break
            curr = curr.next
        # 不论是中间break出来还是到第k个为空，都说明不够k个，不用翻转
        if curr is None:
            return head

        else:  # 如果不为空，则说明够k个，这组要翻转
            curr = head  # curr还是指向头部
            for i in range(k):
                tem = curr.next  # 先保留下一个节点的引用，如果先给next赋值则就链表就断了找不到下一个节点
                curr.next = pre  # 此时保留过下一个节点的引用，可以让下一个指针指向前一个做翻转操作了
                pre = curr  # 这时候就可以把前一个指针前移，把当前指针前移， 这里的顺序也重要，先移后面的，否则也找不到前面一个的位置了
                curr = tem  # 此时curr是下一组开始的位置， pre是当前排完这组开始的位置， head是排完这组结束的位置
            head.next = self.reverseKGroup(curr, k)  # 所以需要用排完这组的结束的位置指向将要排的一组的开始的位置
        return pre  # 返回当前组开始的位置

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
            count = k  # 作为k的计数器
            s = []  # 生成一个空列表当做栈
            curr = head  # curr指向头结点
            while count and curr:  # 查看计数和当前节点
                s.append(curr)  # 把curr节点推入栈中
                curr = curr.next  # curr往前移动
                count -= 1  # 计数器-1，k个中已经有一个进入栈中

            if count:  # 如果count不为空但是现在退出了循环，那么也就是上面终止循环的条件是curr变空了，但是还不够k个，所以直接跳出主循环，不翻转
                p.next = head
                break

            # 否则就是因为count=0退出的上面循环，那么现在curr停在了k+1的位置
            while s:  # 只要s不空则一个一个推出里面的节点
                p.next = s.pop()  # p的next指向推出的节点
                p = p.next  # p向前移动， 直到s里的节点推出干净， 此时p指向这一组的最后一个节点，对于剩下的所有节点来说是dummyhead

            # 连接剩下的链表， p.next 指向k+1的位置，这个如果放在循环外面可能会出现错误，因为上面break的话curr不是k+1的位置，而是None,导致连接错误
            p.next = curr
            head = curr  # 这时候要把head放到下一段头结点的位置
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
