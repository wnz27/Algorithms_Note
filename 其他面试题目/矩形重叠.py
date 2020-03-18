'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-18 01:12:09
@LastEditTime: 2020-03-18 10:36:15
@FilePath: /Algorithms_Note/其他面试题目/矩形重叠.py
@description: type some description
'''
'''
矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，
(x2, y2) 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形
不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。
示例 1：
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
示例 2：
输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false
说明：
两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
矩形中的所有坐标都处于 -10^9 和 10^9 之间。
'''
class Solution(object):
    def isRectangleOverlap1(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # 上下左右边界法
        return not (rec1[1] >= rec2[3] or
                    rec1[0] >= rec2[2] or 
                    rec1[3] <= rec2[1] or 
                    rec1[2] <= rec2[0])
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # 映射法
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))
