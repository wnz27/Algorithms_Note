'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-16 23:10:52
@LastEditTime: 2020-03-17 10:40:53
@FilePath: /Algorithms_Note/其他面试题目/LRU.py
@description: type some description
'''
'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，
则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，
从而为新的数据值留出空间。
进阶:
你是否可以在 O(1) 时间复杂度内完成这两种操作？
示例:
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
'''
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.pre = None
        self.next = None

class DoubleLinked:
    def __init__(self):
        self.__size = 0
        self.dummyhead = Node(None, None)
        self.tail = None
    
    def addFirst(self, k, v):
        if self.size == 0:
            new_node = Node(k, v)
            self.dummyhead.next = new_node
            new_node.pre = self.dummyhead
            self.tail = new_node
        else:
            new_node = Node(k, v)
            self.dummyhead.next.pre = new_node
            new_node.next = self.dummyhead.next
            self.dummyhead.next = new_node
            new_node.pre = self.dummyhead
        self.__size += 1

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.__size -= 1

    def removeLast(self):
        if self.size == 0:
            return None
        else:
            tem = self.tail
            self.tail.pre.next = None
            self.tail = self.tail.pre
            tem.pre = None
            self.__size -= 1
            return tem

    @property
    def size(self):
        return self.__size

class LRUCache:
    def __init__(self, capacity):
        self.hashmap = {}       # k:node
        self.cache = DoubleLinked()
        self.cap = capacity
    
    def get(self, k):
        if k not in self.hashmap:
            return -1
        else:
            val = self.hashmap.get(k).v
            self.put(k, val)
            return val

    def put(self, k, v):
        new_node = Node(k, v)   # 先做出新节点
        if k in self.hashmap:
            self.cache.remove(self.hashmap.get(k))
            self.cache.addFirst(k)
            self.hashmap[k] = new_node
        else:
            if self.cap == self.cache.size:
                last = self.cache.removeLast()
                del self.hashmap[last.k]
            self.cache.addFirst(k, v)
            self.hashmap[k] = new_node
        

