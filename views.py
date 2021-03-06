# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:40:23 2018

@author: Administrator
"""

import random
import IPPool
import requests
import time
import Global
from threading import Lock

#存储添加的url
urllist=[]
#线程锁
lock=Lock()


def work():
    global urllist
    if Global.thread_mark:
        #检测IP池是否为空
        if not IPPool.getramip():
            Global.instatesinf('等待ip...'.decode('utf-8'))
            time.sleep(2)
            return
        #随机选择Url
        url=random.choice(urllist)
        #随机选择代理ip
        IP_dic=IPPool.getramip()
        #将ip设置为proxies格式
        proxy=get_proxy(IP_dic["ip"])
        try:
            #尝试以代理身份访问Url，时限为5秒，超时返回false
            response=requests.get(url,proxies=proxy,timeout=5)
            Global.instatesinf("成功点击~~Nice".decode('utf-8'))
            #此代理成功访问，将其times值设为-2
            IPPool.update(IP_dic,1)
        except:
            #fangwen失败，将其times值加1
            Global.instatesinf("啊偶，无法连接目标网页...".decode('utf-8'))
            IPPool.update(IP_dic,0)
        #如果times值超过最大忍耐次数，则将其从ip池中删除
        if not IPPool.checktimes(IP_dic):
            lock.acquire()
            IPPool.delip(IP_dic)
            lock.release()

    
#从Url池中获取随机Url
def getrampage():
    global webpage
    random.choice(urllist)
#向Url池中添加Url   
def filllist(URL):
    global pagelist
    urllist.append(URL)
#根据得到的代理ip，设置proxy的格式 
def get_proxy(ip):   
    proxy_ip='http://'+ip  
    proxy_ips='https://'+ip  
    proxy = {'https': proxy_ips, 'http': proxy_ip}  
    return proxy
    
