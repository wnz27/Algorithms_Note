#! -*- encoding=utf-8 -*-
from otherLearn.pool import ThreadPool as tp
from operateSystem.task import AsyncTask
import socket
import json

class ProcessTask(AsyncTask):
    def __init__(self, packet, *args, **kwargs):
        self.packet = packet
        AsyncTask(func=self.process, *args, **kwargs)
    def process(self):
        pass


class Server:
    def __init__(self):
        # 工作协议类型、套接字类型、工作具体的协议
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        '''
        mac的shell里把用这个命令
        ifconfig en0
        里面有一项叫inet后面就是你电脑的ip
        '''
        self.ip = '10.148.180.108'
        self.port = 8888
        self.sock.bind((self.ip,self.port,))

        # 设置为混杂模式
        self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        self.pool = tp(10)
        self.pool.start()
    def loop_server(self):
        while True:
            # 1、接受
            packet, addr = self.sock.recv(65535)
            # 2、生成task
            task = ProcessTask(packet)
            # 3、提交
            self.pool.put(task)
            # 4、获取结果
            result = task.get_result()
            result = json.dumps(
                result,
                indent=4
            )
            print(result)
        pass

if __name__ == "__main__":
    server = Server()
    server.loop_server()


