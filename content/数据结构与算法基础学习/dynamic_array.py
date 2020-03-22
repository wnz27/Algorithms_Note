'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-02 18:23:10
@LastEditTime: 2020-03-07 15:37:09
@FilePath: /Algorithms_Note/数据结构与算法基础学习/dynamic_array.py
@description: type some description
'''
class DynamicArray:
    '''
    自己封装动态数组
    '''
    def __init__(self, capacity = 20):
        '''
        构造函数，
        初始化数组，为传容量默认20
        '''
        self.__l = [None] * capacity
        self.__size = 0
    
    @property
    def getCapacity(self):
        '''
        获取数组容量
        '''
        return len(self.__l)
    
    def getSize(self):
        '''
        获取现在数组中元素个数
        '''
        return self.__size
    
    def isEmpty(self):
        '''
        数组是否为空
        '''
        return self.__size == 0

    def add(self, index, e):
        '''
        在索引位置插入一个新元素
        '''
        if index < 0 or index > self.__size:  # 如果索引越界，抛出异常
            raise IndexError('Add failed. Require index >=0 and index <= size!')
        if index == self.getCapacity:            # 如果数组容量满了，则先进行扩容操作
            self.resize_array(2 * self.getCapacity)
        for i in range(self.__size-1, index-1, -1):
            self.__l[i + 1] = self.__l[i]
        self.__l[index] = e
        self.__size += 1
    
    def addLast(self, e):
        '''
        在数组最后加入一个元素
        '''
        self.add(self.__size, e)
    
    def addFirst(self, e):
        '''
        在数组开头加入一个元素
        '''
        self.add(0, e)
            
    def get(self, index):
        '''
        拿到索引位置的元素
        '''
        if index < 0 or index >= self.__size:
            raise IndexError('Get failed! Index is illegal!!!')
        return self.__l[index]
    
    def getFirst(self):
        return self.get(0)
    
    def getLast(self, index):
        return self.get(self.__size - 1)
    
    def set(self, index, e):
        '''
        修改索引位置的元素
        '''
        if index < 0 or index >= self.__size:
            raise IndexError('Get failed! Index is illegal!!!')
        self.__l[index] = e
    
    def contains(self, e):
        '''
        查找数组中是否有元素e
        '''
        for i in self.__l:
            if i == e:
                return True
        return False
    
    def find(self, e):
        '''
        查找元素e所在的索引，如果不存在元素e，返回-1
        '''
        for i in range(self.__size):
            if self.__l[i] == e:
                return i
        return -1
    
    def remove(self, index):
        '''
        从数组中删除索引index位置的元素
        返回删除的元素
        '''
        if index < 0 or index >= self.__size:
            raise IndexError("remove failed! index is illegal!!!")
        res = self.__l[index]
        for i in range(self.__size-1, index, -1):
            self.__l[i-1] = self.__l[i]
        self.__size -= 1
        self.__l[index] = None  # 把index位置的值再置空
        if self.__size == int(self.getCapacity / 4) and int(self.getCapacity/2) != 0:  # 缩容操作
            self.resize_array(int(self.getCapacity / 2))
        return res
    
    def removeLast(self):
        return self.remove(self.__size - 1)
    
    def removeFirst(self):
        return self.remove(0)
    
    def removeElement(self, e):
        index = self.find(e)
        if index != -1:
            return self.remove(index)
    
    def resize_array(self, resizeLength):
        '''
        数组扩容，python
        '''
        tem = self.__l
        newArray = [0] * resizeLength
        self.__l = newArray
        for i in range(len(tem)):
            self.__l[i] = tem[i]
    
    def __str__(self):
        res = '['
        for i in range(self.__size):
            res += str(self.__l[i])
            if i != self.__size-1:
                res += ', '
            else:
                res += ']'
        return 'dynamic_array: {}, size: {}, capacity: {}'.format(res, self.__size, self.getCapacity)

    def __repr__(self):
        res = '['
        for i in range(self.__size):
            res += str(self.__l[i])
            if i != self.__size-1:
                res += ', '
            else:
                res += ']'
        super_repr = super.__repr__
        return '{}----dynamic_array: {}, size: {}, capacity: {}'\
                .format(super_repr, res, self.__size, self.getCapacity)

    
a = DynamicArray(3)
a.addFirst(2)
a.addFirst(1)
a.addLast(10)
print(a)
a.add(3, 99)
a.add(2, 678)
print(a)


        
    