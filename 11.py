import sys
from for11 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.chet = []
        self.nechet = []
        self.all = []

    def initUI(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open('inputstr.txt', 'r', encoding='utf-8') as f:
            for str in f:
                str = str.rstrip('\n')
                self.all.append(str)

            self.nechet = self.all[::2]
            self.chet = self.all[1::2]
            self.str1 = ''
            for elem in self.chet:
                self.str1 = self.str1 + ' ' + elem + '\n'
            for elem1 in self.nechet:
                self.str1 = self.str1 + ' ' + elem1 + '\n'

            self.textBrowser.setText(self.str1)




sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())












