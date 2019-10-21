#! -*- encoding=utf-8 -*-
import uuid

# 基本任务对象
class Task:
    def __init__(self, func, *args, **kwargs):
        # callable:任务具体逻辑，通过函数引用传递进来
        self.callable = func
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs

    
    def __str__(self):
        return 'Task id: ' + str(self.id)
    
def my_fuction():
    print("this is a task test.")

# if __name__ == "__main__":
#     task = Task(func=my_fuction)      # 这个task就可以执行函数里的逻辑
#     print(task)
    
    

