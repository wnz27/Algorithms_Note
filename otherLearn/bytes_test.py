#! -*- encoding=utf-8 -*-
# pyhotn使用struct这个包来实现字节序列操作
import struct

# 八个字节
bin_str = b'ABCD1234'
print(bin_str)
'''
我们是通过struct这个包来对字节序列来操作的
把八个字节每个字节都转化成一个整数，用B来变整数
>大于号表示大端字节序
'''
big_byte1 = struct.unpack('>BBBBBBBB', bin_str)
print(big_byte1)     # 各个字符的ASCII码

'''
使用H,两个字节转换为一个整数的
'''
big_byte2 = struct.unpack('>HHHH', bin_str)
print(big_byte2)
'''
使用L,四个字节转换为一个整数
'''
big_byte3 = struct.unpack('>LL', bin_str)
print(big_byte3)
'''
使用s，转化为8个ASCII码的字符
'''
big_byte4 = struct.unpack('>8s', bin_str)
print(big_byte4)
'''
混合的使用解析
'''
big_byte = struct.unpack('>BBHL', bin_str)
print(big_byte)