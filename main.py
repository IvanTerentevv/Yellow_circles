import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file.ui', self)
        self.btn.clicked.connect(self.do)
        self.figure = ''

    def do(self):
        self.x = randint(0, 800)
        self.y = randint(0, 600)
        self.figure = 'circle'
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        if self.figure == 'circle':
            qp.setBrush(QColor('yellow'))
            a = randint(1, 100)
            qp.drawEllipse(self.x, self.y, a, a)
            self.figure = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())