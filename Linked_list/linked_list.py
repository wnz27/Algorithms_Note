#! -*- encoding=utf-8 -*-
class MyNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return '{%d}' % (self.val)
    
    def __repr__(self):
        return '{%d}' % (self.val)

class MyLinkedList(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 5
        self.size = 0
        self.head = None
        self.tail = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.capacity:
            return -1
        else:
            cur = self.head
            for i in range(0, index):
                cur = cur.next
            return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = MyNode(val)
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.size += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = MyNode(val)
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.size += 1
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        node = MyNode(val)
        if index <= 0:
            self.addAtHead(val)
        elif index == self.capacity:
            self.addAtTail(val)
        elif index > self.capacity:
            return
        else:
            cur = self.head
            for i in range(0, index):
                cur = cur.next
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        pass
    
    # 打印当前链表
    def print(self):
        p = self.head
        line = ''   # 使用一个变量存储链表的字符串
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += "=>"
        print (line)


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.print()
print(obj.get(1))
obj.deleteAtIndex(1)
obj.print()
print(obj.get(1))