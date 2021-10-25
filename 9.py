import sys
import random
from randomstr import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.lines = []
        with open('inputstr.txt', 'r', encoding='utf-8') as file:
            for line in file:
                self.lines.append(line)

    def initUI(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        rand = random.choice(self.lines)
        self.lineEdit.setText(rand)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
