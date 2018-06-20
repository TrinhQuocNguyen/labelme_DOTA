#-*- coding:utf-8 -*-
#######pyqt绘制点，线，矩形，圆
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from random import *
class MyWindow(QDialog,QWidget):
    def __init__(self,parent = None):
        super(MyWindow,self).__init__(parent)
        self.resize(800,800)
        self.mainlayout = QGridLayout(self)

    def paintEvent(self, e):########画图事件，每次update都会进入，想画啥根据注释进行,双击重画
        qp = QPainter()
        qp.begin(self)

        qp.setPen(QPen(Qt.red,10))   ######可以试下画刷 setBrush,10指定点的大小
        qp.drawPoint(1, 1)

        #self.drawLines(qp)######画线
        #self.drawPoints(qp)  ###画点
        #self.drawRect(qp)    ##画矩形
        #self.drawEllipse(qp)  ##画圆,椭圆
        qp.end()

    def mouseDoubleClickEvent(self, *args, **kwargs):
        self.update()

    def drawPoints(self, qp):
        qp.setPen(QPen(Qt.red,10))   ######可以试下画刷 setBrush,10指定点的大小
        qp.drawPoint(1, 1)

    def drawLines(self,qp):#######画线
        loc_list = []
        for i in xrange(4):
            loc_list.append((randint(0,self.width()),randint(0,self.height())))########获取随机点
        color = choice([Qt.black,Qt.white,Qt.darkGray,Qt.red,Qt.green,Qt.blue,Qt.cyan,Qt.magenta,Qt.yellow,Qt.darkRed,Qt.darkGreen,Qt.darkBlue,Qt.darkCyan,Qt.darkMagenta,Qt.darkYellow])
        qp.setPen(QPen(color, randint(0,10), randint(1,6)))####前一个random是线条粗线，后一个random是线条类型
        for i in xrange(4):
            qp.drawLine(loc_list[i][0],loc_list[i][1],loc_list[(i+1)%4][0],loc_list[(i+1)%4][1])

    def drawRect(self,qp):
        qp.setPen(QPen(Qt.red,2,Qt.SolidLine))
        qp.drawRect(200,200,400,400)

    def drawEllipse(self,qp):########椭圆，圆
        qp.setPen(QPen(Qt.blue,2,Qt.SolidLine))
        qp.drawEllipse(100,200,300,300)

app=QApplication(sys.argv)
window=MyWindow()
window.show()
app.exec_()