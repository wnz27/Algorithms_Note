#! -*- coding=utf-8 -*-
# Least Recently Use
from DoubleLinkList import DoubleLinkedList, Node

class LRUCache(object):
    """
    LRU缓存算法采取的缓存置换策略是， 当缓存空间满时新来的数据置换到未使用时间最长的那个，实现中采用双向链表， 
    将每次访问到的数据放在链表的最前端，从而保证链表里的数据是按使用时间有序的。
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.size = 0
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self.list.append_front(node)
            return node.value
        else:
            return -1
    
    def put(self, key, value):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append_front(node)
        else:
            node = Node(key, value)
            # 链表缓存已经满了
            if self.size == self.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)
                self.size -= 1
            # 链表缓存还没有满
            self.list.append_front(node)
            self.map[key] = node
            self.size += 1
    
    def print(self):
        self.list.print()
    
# 测试
if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(2,2)
    cache.print()
    cache.put(1,1)
    cache.print()
    cache.put(3,3)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()

'''
输出：
{2: 2}
{1: 1}=>{2: 2}
{3: 3}=>{1: 1}
1
{1: 1}=>{3: 3}
-1
{1: 1}=>{3: 3}
3
{3: 3}=>{1: 1}
'''    
