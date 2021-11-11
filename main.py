from PyQt5 import uic
import random

from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setMinimumSize(QSize(700, 700))
        MainWindow.setMaximumSize(QSize(700, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pb = QPushButton(self.centralwidget)
        self.pb.setObjectName(u"pb")
        self.pb.setGeometry(QRect(320, 320, 60, 60))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pb.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


class Ex(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        self.pb.clicked.connect(self.run)
        self.circles = []

    def run(self):
        self.circles.clear()
        for i in range(random.randrange(1, 5)):
            s = random.randrange(50, 150)
            x = random.randrange(s, 700 - s)
            y = random.randrange(s, 700 - s)
            c = QColor(random.randrange(255), random.randrange(255), random.randrange(255))
            self.circles.append((x, y, s, c))
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        for i in self.circles:
            qp.setBrush(i[3])
            qp.drawEllipse(i[0], i[1], i[2], i[2])
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec())
