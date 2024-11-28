import sys
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt6 import uic


class Euglenophyta(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.goida_create_circle.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        d = randint(1, 1000)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(0, 800), randint(0, 600), d // 2, d // 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Euglenophyta()
    ex.show()
    sys.exit(app.exec())
