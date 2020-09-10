#! -*- coding=utf-8 -*-
# least frequently used
from DoubleLinkList import DoubleLinkedList, Node

class LFUNode(Node):
    def __init__(self, key, value):
        self.freq = 1   # 频率
        super().__init__(key, value)
    
class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        # key: 频率， value: 频率对应的双向链表
        self.freq_map = {}
        self.size = 0
    
    # 更新节点频率的操作
    def __update_freq(self, node):
        freq = node.freq
        # 删除操作
        node = self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]

        # 更新操作
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].append(node)
    
    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.__update_freq(node)
        return node.value
    
    def put(self, key, value):
        if self.capacity == 0:
            return
        # 缓存命中的情况
        if key in self.map:     # 节点在map里
            node = self.map.get(key)
            node.value = value
            self.__update_freq(node)
        # 缓存没有命中的情况
        else:                   # 节点不在map里
            if self.capacity == self.size:   # 如果缓存已经满了
                min_freq = min(self.freq_map)  # 找出最小频率
                node = self.freq_map[min_freq].pop()
                del self.map[node.key]
                self.size -= 1
            node = LFUNode(key, value)
            self.map[key] = node
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            self.freq_map[node.freq].append(node)
            self.size += 1
    
    def print(self):
        print("*" * 40)
        for k, v in self.freq_map.items():
            print('Freq = %d' %k)
            self.freq_map[k].print()
        print("*" * 40)
        print()
    
# 测试
if __name__ == "__main__":
    cache = LFUCache(4)
    cache.put(1,1)
    cache.print()
    cache.put(2,2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.put(3,3)
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
    cache.put(4,4)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(3))
    cache.print()
    print(cache.get(4))
    cache.print()
    cache.put(5,5)
    cache.print()
    print(cache.get(6))
    cache.print()

    '''
    输出：
    ****************************************
    Freq = 1
    {1: 1}
    ****************************************

    ****************************************
    Freq = 1
    {1: 1}=>{2: 2}
    ****************************************

    1
    ****************************************
    Freq = 1
    {2: 2}
    Freq = 2
    {1: 1}
    ****************************************

    ****************************************
    Freq = 1
    {2: 2}=>{3: 3}
    Freq = 2
    {1: 1}
    ****************************************

    2
    ****************************************
    Freq = 1
    {3: 3}
    Freq = 2
    {1: 1}=>{2: 2}
    ****************************************

    3
    ****************************************
    Freq = 2
    {1: 1}=>{2: 2}=>{3: 3}
    ****************************************

    ****************************************
    Freq = 2
    {1: 1}=>{2: 2}=>{3: 3}
    Freq = 1
    {4: 4}
    ****************************************

    1
    ****************************************
    Freq = 2
    {2: 2}=>{3: 3}
    Freq = 1
    {4: 4}
    Freq = 3
    {1: 1}
    ****************************************

    3
    ****************************************
    Freq = 2
    {2: 2}
    Freq = 1
    {4: 4}
    Freq = 3
    {1: 1}=>{3: 3}
    ****************************************

    4
    ****************************************
    Freq = 2
    {2: 2}=>{4: 4}
    Freq = 3
    {1: 1}=>{3: 3}
    ****************************************

    ****************************************
    Freq = 2
    {4: 4}
    Freq = 3
    {1: 1}=>{3: 3}
    Freq = 1
    {5: 5}
    ****************************************

    -1
    ****************************************
    Freq = 2
    {4: 4}
    Freq = 3
    {1: 1}=>{3: 3}
    Freq = 1
    {5: 5}
    ****************************************
    '''
