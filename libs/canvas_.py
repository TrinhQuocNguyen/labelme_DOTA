# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
from libs.shape import Shape

class MouseEvent(QMainWindow):
    def __init__(self, parent=None):
        super(MouseEvent, self).__init__(parent)
        self.resize(800, 800)
        self.count = 0
        self.drawingLineColor = QColor(0, 0, 255)
        self.drawingRectColor = QColor(0, 0, 255)
        self.line = Shape(line_color=self.drawingLineColor)

        labelStatus = QLabel();
        labelStatus.setText(self.tr("Mouse Position:"))
        labelStatus.setFixedWidth(100)
        self.labelMousePos = QLabel();
        self.labelMousePos.setText(self.tr(""))
        self.labelMousePos.setFixedWidth(100)
        self._painter = QPainter()
        self.sBar = self.statusBar()
        self.sBar.addPermanentWidget(labelStatus)
        self.sBar.addPermanentWidget(self.labelMousePos)


    def mouseMoveEvent(self, e):
        self.labelMousePos.setText("(" + QString.number(e.x()) + "," + QString.number(e.y()) + ")")
        self.update()

    def mousePressEvent(self, e):
        str = "(" + QString.number(e.x()) + "," + QString.number(e.y()) + ")"
        if e.button() == Qt.LeftButton:
            self.sBar.showMessage(self.tr("Mouse Left Button Pressed:") + str)
            x = QString.number(e.x()).toInt()[0]
            y = QString.number(e.y()).toInt()[0]
            q = QPoint(x, y)
            print(x, y)
            if self.count == 4:
                self.count = 0
                self.line.clear()
            else:
                self.count = self.count + 1
            self.line.addPoint(q)
            self.update()
        elif e.button() == Qt.RightButton:
            self.sBar.showMessage(self.tr("Mouse Right Button Pressed:") + str)
        elif e.button() == Qt.MidButton:
            self.sBar.showMessage(self.tr("Mouse Middle Button Pressed:") + str)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(QPen(Qt.red, 5))  ######可以试下画刷 setBrush,10指定点的大小

        l = len(self.line.points)
        if l == 0:
            qp.end()
        elif l < 4:
            p = QPoint(self.line.points[0])
            qp.drawPoint(p)
            for i in range(0, l-1):
                p = QPoint(self.line.points[i%4])
                q = QPoint(self.line.points[(i+1)%4])
                qp.drawLine(q, p)
        else:
            for i in range(0, 3):
                p = QPoint(self.line.points[i%4])
                q = QPoint(self.line.points[(i+1)%4])
                qp.drawLine(q, p)
            p = QPoint(self.line.points[3])
            q = QPoint(self.line.points[0])
            qp.drawLine(q, p)
        # self.drawLines(qp)######画线
        # self.drawPoints(qp)  ###画点
        # self.drawRect(qp)    ##画矩形
        # self.drawEllipse(qp)  ##画圆,椭圆
        qp.end()


app = QApplication(sys.argv)
dialog = MouseEvent()
dialog.show()
app.exec_()