'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-07 07:13:34
@LastEditTime: 2020-03-07 07:14:01
@FilePath: /Algorithms_Note/《剑指offer刷刷刷刷》/队列最大值.py
@description: type some description
'''
'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：
输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
'''