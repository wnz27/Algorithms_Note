#! -*- encoding=utf-8 -*-
from DoubleLinkList import DoubleLinkedList, Node

class FIFOCache(object):
    """
    ## FIFO缓存算法

    其中FIFO最为简单，其基本假设就是最近被加载进来的数据下次使用到的可能性大于之前被加载进来的数据，对于符合这种假设的场景较为适用。
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)
    
    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map.get(key)
            return node.value
        
    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append(node)
        else:
            if self.size == self.capacity:
                node = self.list.pop()
                del self.map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.list.append(node)
            self.map[key] = node
            self.size += 1
    
    def print(self):
        self.list.print()

# 测试
if __name__ == '__main__':
    cache = FIFOCache(2)
    cache.put(1,1)
    cache.print()
    cache.put(2,2)
    cache.print()
    print(cache.get(1))
    cache.put(3,3)
    cache.print()
    print(cache.get(2))
    cache.print()
    cache.put(4,4)
    cache.print()
    print(cache.get(1))

    '''
    输出：
    {1: 1}
    {1: 1}=>{2: 2}
    1
    {2: 2}=>{3: 3}
    2
    {2: 2}=>{3: 3}
    {3: 3}=>{4: 4}
    -1
    '''
