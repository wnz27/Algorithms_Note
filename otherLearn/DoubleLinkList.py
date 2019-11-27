#! -*- encoding=utf-8 -*-
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
    def __str__(self):
        val = '{%d: %d}' % (self.key, self.value)
        return val
    
    def __repr__(self):
        val = '{%d: %d}' % (self.key, self.value)
        return val
    
class DoubleLinkedList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
    
    # 从头部添加节点
    def __add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = None
            self.head.prev = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1
        return node
    
    # 往尾部添加节点
    def __add_tail(self,node):
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.next = None
            self.tail.prev = None
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node
    
    # 从尾部删除节点的功能
    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:   # 这个节点是否有上一个节点
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node
    
    # 从头部删除节点的功能
    def __del_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:  # 这个节点是否有下一个节点
            self.head = node.next
            self.head.prev = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # 删除任意节点
    def __remove(self, node):
        # 如果node=None，默认删除尾部节点
        if not node:
            node = self.tail
            '''
            self.tail.prve.next = None
            '''
        if node == self.head:
            self.__del_head()
        elif node == self.tail:
            self.__del_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node

    ############## 公共接口方法 ############################
    # 弹出头部节点
    def pop(self):
        return self.__del_head()
    
    # 往尾部添加节点
    def append(self, node):
        return self.__add_tail(node)
    
    # 往头部添加节点
    def append_front(self, node):
        return self.__add_head(node)

    # 删除节点
    def remove(self, node=None):
        return self.__remove(node)
    
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


# 测试
if __name__ == '__main__':
    l = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        node = Node(i,i)
        nodes.append(node)
    
    l.append(nodes[0])
    l.print()
    l.append(nodes[1])
    l.print()
    l.pop()
    l.print()
    l.append(nodes[2])
    l.print()
    l.append_front(nodes[3])
    l.print()
    l.append(nodes[4])
    l.print()
    l.remove(nodes[2])
    l.print()
    l.remove()
    l.print()
    '''
    输出：
    {0: 0}
    {0: 0}=>{1: 1}
    {1: 1}
    {1: 1}=>{2: 2}
    {3: 3}=>{1: 1}=>{2: 2}
    {3: 3}=>{1: 1}=>{2: 2}=>{4: 4}
    {3: 3}=>{1: 1}=>{4: 4}
    {3: 3}=>{1: 1}
    '''