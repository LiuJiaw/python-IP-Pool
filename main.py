# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 17:41:29 2018

@author: Administrator
"""

import sys
from PyQt4 import QtCore,QtGui,uic
import views
import Global
import IPPool
import chardet

qtCreatorFile = "UI.ui" 
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#我的主界面类，继承于QMainWindow
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        #分别对QMainWindow与我的MainWindow进行初始化
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #分别设置按钮点击后对应的槽函数
        self.addpushButton.clicked.connect(self.add)
        self.clearButton.clicked.connect(self.clear)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.help_()
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.Update)
        self.timer.start(200)
       
    #实现将所需加入的Url
    def add(self):
        url=self.URLEdit.text()
        self.textEdit.append("已添加：".decode('utf-8')+url) 
        self.URLEdit.clear()
        views.filllist(url)
    #清除已输入的信息   
    def clear(self):
        self.tidEdit.clear()
        self.portsEdit.clear()
        self.exclude_portsEdit.clear()
        self.numEdit.clear()
        self.URLEdit.clear()
        self.textEdit.clear()
    #开始进行    
    def start(self):
        Global.settidValue(self.tidEdit.text())
        Global.setoperatorValue(self.operatorcomboBox.currentText())
        Global.setportsValue(self.portsEdit.text())
        Global.setexclude_portsValue(self.exclude_portsEdit.text())
        Global.setprotocolValue(self.protocolcomboBox.currentText())
        Global.setcategoryValue(self.categorycomboBox.currentText())
        Global.setsortbyValue(self.sortbycomboBox.currentText())
        Global.setnumValue(self.numEdit.text())
        Global.settimesValue(self.timesEdit.text())
        Global.setspeedValue(self.speedcomboBox.currentText())
        Global.setapiValue()
        IPPool.thread_mark=1
        #IP池维护操作开始执行
        IPPool.start()
        views.thread_mark=1
        #页面访问操作开始执行
        views.start()
    #显示help文档信息
    def help_(self):
        f=open("help.txt","r")
        text=f.read()
        f.close()
        type_=chardet.detect(text)
        self.textEdit.append(text.decode(type_["encoding"]))
    #暂停所有线程   
    def stop(self):
        Global.thread_mark=0
    #实时显示当前状态信息    
    def Update(self):
        global message_queue
        if Global.getsize():
            text=Global.outstatesinf()
            self.textEdit.append(text)
    

 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
