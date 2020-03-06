# -*- coding:utf-8 -*-

#QUESTION DESCRIPTION
'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, 
which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
'''
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        resultPosition = [0,0]
        for letter in moves:
            self.judgeMove(resultPosition,letter)
        if resultPosition == [0,0]:
            return True
        else:
            return False
    
    def judgeMove(self,location,moveStyle):
        '''
        根据字符命令移动位置坐标
        '''
        if moveStyle == "U":
            location[1]+=1
        elif moveStyle == "D":
            location[1]-=1
        elif moveStyle == "L":
            location[0]+=1
        else:
            location[0]-=1

