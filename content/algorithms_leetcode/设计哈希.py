# -*- coding: utf-8 -*-
# @UpdateTime    : 2021/3/13 11:32
# @Author    : 27
# @File    : 设计哈希.py

"""
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：

void add(key) 向哈希集合中插入值 key 。
bool contains(key) 返回哈希集合中是否存在这个值 key 。
void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
 
示例：

输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.contents = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.contents.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.contents.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for i in self.contents:
            if i == key:
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(2)
    obj.contains(2)
    obj.remove(2)
    res = obj.contains(2)
    print(res)
    pass
