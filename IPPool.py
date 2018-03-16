# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:37:18 2018

@author: Administrator
"""

import Global
import random
import requests
import re

#IP池，该.py文件中均为对IP池操作的函数
IPPool=[]


def work():
    global IPPool
    if Global.thread_mark:
        if poolmissnum()>0:
            fillpool()
#       showme()

#检测IP池是否为满,返回IP池缺少的个数
def poolmissnum():
    global IPPool
    return int(Global.getnumValue())-len(IPPool)
 
#将新的IP填充至ip池   
def fillpool():
    global IPPool
    api=Global.getapiValue()+'&num='.decode('utf-8')+str(poolmissnum()).decode('utf-8')   
    respose=requests.get(api)
    data=respose.text
    List=re.findall('[0-9\.\:]+',data)
    for row in List:
        IP_dic={"ip":row,
                "times":0
        }
        IPPool.append(IP_dic)
        a=("已将%s投入IP池".decode('utf-8'))%(IP_dic["ip"])
        Global.instatesinf(a)

#删除失效的ip字典
def delip(IP_dic):
    global IPPool
    try:
        IPPool.remove(IP_dic)
    except:
        Global.instatesinf("IP池中已无此IP".decode('utf-8'))
    a=("已将%s清除出IP池".decode('utf-8'))%(IP_dic["ip"])
    Global.instatesinf(a)
    
#获取IP池中随机IP
def getramip():
    global IPPool
    if len(IPPool)==0:
        return 0
    return random.choice(IPPool)
    
#检测ip无效请求次数
def checktimes(IP_dic):
    if IP_dic["times"]>=Global.gettimesValue():
        return 0
    return 1
#更新IP连续访问失败次数 
def update(IP_dic,state):
    global IPPool
    try:    
        a=IPPool.index(IP_dic)
    except:
        return
    if state:    
        IPPool[a]["times"]=-2
        return
    IPPool[a]["times"]+=1
    
#展示IP池中IP信息   
def showme():
    global IPPool
    for row in IPPool:
        print row["ip"],row["times"]
    
