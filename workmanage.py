# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:56:28 2018

@author: Administrator
"""

import Queue  
import threading
import views
import IPPool
import views
import Global
  
class WorkManager(object):  
    def __init__(self):  
        self.work_queue = Queue.Queue()  
        self.threads=[]  
        self.__init_work_queue()  
        self.__init_thread_pool()  
  
    #初始化线程
    def __init_thread_pool(self):  
        for i in range(0,6):  
            self.threads.append(Work(self.work_queue))
  
    #初始化工作队列 
    def __init_work_queue(self,):  
        #我设置了5个线程来对页面进行访问，一个线程对ip池进行维护
        for i in range(0,5):  
            self.add_job(views.work)
        self.add_job(IPPool.work)
  
    #添加一项工作入队
    def add_job(self, func):  
        self.work_queue.put(func)#任务入队，Queue内部实现了同步机制  

  
class Work(threading.Thread):  
    def __init__(self, work_queue):  
        threading.Thread.__init__(self)  
        self.work_queue = work_queue  
        self.start()  
  
    def run(self):  
        while Global.thread_mark:  
            #任务异步出队，Queue内部实现了同步机制 
            func=self.work_queue.get(block=False)
            self.work_queue.put(func)
            func()   
            print Global.thread_mark
            
def start():
    work=WorkManager()
  
