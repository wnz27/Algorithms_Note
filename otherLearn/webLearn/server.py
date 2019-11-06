#! -*- encoding=utf-8 -*-
import socket

def server():
    # 创建socket
    s = socket.socket()
    host = '127.0.0.1'  # 主机
    port = 6666
    # 绑定套接字
    s.bind((host, port))

    # 监听
    s.listen(5)
    while True:
        c, addr = s.accept()
        print('Connect addr:%s and client:%s' %(addr, c))
        c.send(b'Welcome to my course.')
        c.close()

if __name__ == "__main__":
    server()
