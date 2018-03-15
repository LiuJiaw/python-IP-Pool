# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:35:32 2018

@author: Administrator
"""

from Queue import Queue


#订单号
tid=''
#运行商
operator=''
#端口号
ports=''
#排除端口
exclude_ports=''
#最大能够忍耐的无效请求次数
times=''
#支持的协议	
protocol=''
#类别(匿名度)	
category=''
#IP排序，传入speed表示最快优先，time表示最新优先
sortby=''
#ip池容量
num=0
#记录除了提取数量之外的所有参数的api
api=''
#访问百度速度（延时）
speed=''
#消息队列，IP池以及views中的状态信息会进入到此队列
message_queue=Queue()


def instatesinf(text):
    global message_queue
    message_queue.put(text)
    
def outstatesinf():
    global message_queue
    return message_queue.get()
    
def getsize():
    return message_queue.qsize()

def settidValue(Str):
    global tid
    tid=Str
    
def setoperatorValue(Str):
    global operator
    if Str=="任何".decode('utf-8'):
        operator=''
    elif Str=="电信".decode('utf-8'):
        operator='1'.decode('utf-8')
    elif Str=="联通".decode('utf-8'):
        operator='2'.decode('utf-8')
    else:
        operator='3'.decode('utf-8')
    
def setportsValue(Str):
    global ports
    ports=Str
    
def setexclude_portsValue(Str):
    global exclude_ports
    exclude_ports=Str
    
def settimesValue(Str):
    global times
    if str=='':
        times=3
        return
    times=int(Str)
    
def setprotocolValue(Str):
    global protocol
    if Str=='不限制'.decode('utf-8'):
        protocol=''
        return
    protocol='https'.decode('utf-8')
    
def setcategoryValue(Str):
    global category
    if Str=='不限制'.decode('utf-8'):
        category=''
        return
    category='2'.decode('utf-8')
    
def setsortbyValue(Str):
    global sortby
    if Str=='最快优先'.decode('utf-8'):
        sortby=''
        return
    sortby='time'.decode('utf-8')
    
def setnumValue(Str):
    global num
    if num=='':
        num=5
        return
    num=int(Str)
    
def setspeedValue(Str):
    global speed
    if Str=='不限制'.decode('utf-8'):
        speed=''
        return
    speed=Str
    
def setapiValue():
    global api
    api='http://tvp.daxiangdaili.com/ip/?'
    if gettidValue():
        api=api+'tid='+gettidValue()
    if getoperatorValue():
        api=api+'&operator='+getoperatorValue()
    if getportsValue():
        api=api+'&ports='+getportsValue()
    if getexclude_portsValue():
        api=api+'&exclude_ports='+getexclude_portsValue()
    if getprotocolValue():
        api=api+'&protocol='+getprotocolValue()
    if getcategoryValue():
        api=api+'&category='+getcategoryValue()
    if getsortbyValue():
        api=api+'&sortby='+getsortbyValue()
    if getspeedValue():
        api=api+'&delay='+getspeedValue()
        
def gettidValue():
    global tid
    return tid
    
def getoperatorValue():
    global operator
    return operator
    
def getportsValue():
    global ports
    return ports
    
def getexclude_portsValue():
    global exclude_ports
    return exclude_ports
    
def gettimesValue():
    global times
    return times
    
def getprotocolValue():
    global protocol
    return protocol
    
def getcategoryValue():
    global category
    return category
    
def getsortbyValue():
    global sortby
    return sortby
    
def getnumValue():
    global num
    return num
    
def getspeedValue():
    global speed
    return speed
    
def getapiValue():
    global api
    return api