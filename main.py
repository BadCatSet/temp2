from PyQt5 import uic
import random
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pb.clicked.connect(self.run)
        self.circles = []

    def run(self):
        self.circles.clear()
        for i in range(random.randrange(1, 5)):
            s = random.randrange(50, 150)
            x = random.randrange(s, 700 - s)
            y = random.randrange(s, 700 - s)
            self.circles.append((x, y, s))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(100, 100, 0))
        for i in self.circles:
            qp.drawEllipse(i[0], i[1], i[2], i[2])
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec())
