# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
class MainWindow(QtGui.QWidget):
    def __init__(self ,parent=None):
        super(MainWindow,self).__init__(parent)
        # окно без рамок и заголовка, не отображается на панели задач
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.Tool)
        # прозрачный бек окна
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.setAttribute(QtCore.Qt.WA_PaintOnScreen) # работает только в X11
        grid = QtGui.QGridLayout(self)
        self.setLayout(grid)
        label = QtGui.QLabel(text='PRESS THE BUTTON - >') # какойто текст
        label1 = QtGui.QLabel(text='another text') # какойто текст
        btn = QtGui.QPushButton('Close',self)   # кнопака выхода иначе хрен закроеш
        btn.clicked.connect(self.close)
        grid.addWidget(label , 0, 0)
        grid.addWidget(label1 , 1, 1)
        grid.addWidget(btn , 0, 1)
        grid.setAlignment(QtCore.Qt.AlignCenter)
        # привязка к разрешению экрана
        desktop = QtGui.QApplication.desktop()
        screen01 = desktop.primaryScreen() # у меня 2 монитора, определяем главный
        # получаем разрешение нужного монитора
        res = desktop.screenGeometry(screen01)
        # устанавливаем размер откна по размеру монитора
        self.setFixedSize(res.width(), res.height())
        # перемещаем окно чтобы оно заняло весь монитор
        self.move(0, 0)
        self.show()
    def close(self):
        self.hide()
        QtGui.qApp.quit()
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow=MainWindow()
    sys.exit(app.exec_())
