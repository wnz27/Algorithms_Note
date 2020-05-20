# -*- coding:utf-8 -*-
# Create by 27
# @Time : 2020/5/21 01:34
__author__ = '27'
"""
设计一个支持以下两种操作的数据结构：
void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
示例:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:
你可以假设所有单词都是由小写字母 a-z 组成的。
"""


class Node(object):
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.next = {}


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.next:
                curr.next[char] = Node()
            curr = curr.next[char]
        curr.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.__match(self.root, word, 0)

    def __match(self, node, word, index):
        """
        递归
        """
        # 递归出口：
        # 如果索引为单词长度了则说明进来时是最后一个字母了，node就是最后一个字母对应的value的那个node，如果是单词就返回True
        if index == len(word):
            return node.is_word
        # 拿出来当前字符
        char = word[index]
        # 如果字符不等于点，那就找对应下一个节点
        if char != '.':
            if char not in node.next:  # 如果char不在，那么直接返回False
                return False
            # 否则就返回匹配下一个的结果
            return self.__match(node.next[char], word, index+1)
        else:  # 如果char是点，就循环遍历node.next的每一个char对应的节点，调用mach方法
            for char in node.next.keys():
                # 如果匹配到了，返回True
                if self.__match(node.next[char], word, index+1):
                    return True
            # 如果循环遍历完还没有匹配到则返回False
            return False





