'''
@Author: 27
@LastEditors: 27
@Date: 2020-05-20 21:57:37
@LastEditTime: 2020-05-21 00:14:48
@FilePath: /Algorithms_Note/content/数据结构与算法基础学习/Trie字典树/my_trie.py
@description: type some description
'''
class Node:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.next = {}


class MyTrie:
    def __init__(self):
        """
        初始化方法，无需接收任何值
        根也是一个节点，且没有任何数据
        """
        self.root = Node()
        self.size = 0
    
    @property
    def get_size(self):
        """
        获取字典树的大小
        """
        return self.size

    def add_word(self, word):
        """
        接收一个字符串，但是需要把字符串拆成
        一个一个字符添加进字典树
        description: 向字典树中添加一个新的单词，word
        """
        # 先让curr指向当前根节点
        curr = self.root
        for char in word:
            # 先检查下一个节点有没有这个字符
            next_node = curr.next.get(char, None)
            # 如果没有则用这个字符生成一个新节点
            if next_node is None:
                next_node = Node()
                curr.next = {char: next_node}
            # 如果有就把curr移动到下一个，然后进入下一循环
            curr = next_node
        # 这个单词之前没有存进来过，那这个值不会是true
        if not curr.is_word:
            curr.is_word = True
            # 这时才能确认我们添加的是一个新的单词，才把size+1
            self.size += 1
    
    def contains_word(self, word):
        """
        查看单词word是否在trie中
        """
        # 把root找出来
        curr = self.root
        # 遍历word的每个字符
        for char in word:
            # 检查下一个节点有没有这个字符串
            next_node = curr.next.get(char, None)
            if next_node is None:
                return False
            else:
                curr = next_node
        # 这时不能return true，原因比如我们查pan，但是字典里已经有panda了，
        # 所以我们还要判断这个节点的is_word是不是true，是true的话才能返回true
        # 所以直接返回is_word的值即可
        return curr.is_word



            

    

    