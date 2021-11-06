import sys
from for12 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton_3.clicked.connect(self.open)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_edit.clicked.connect(self.edit)

    def open(self):
        with open(self.lineEdit.text(), 'r+', encoding="utf-8") as file:
            self.textEdit.setText(f'{file.read()}')

    def save(self):
        with open(self.lineEdit.text(), 'r+', encoding="utf-8") as file:
            file.write(self.textEdit.toPlainText())

    def edit(self):
        self.textEdit.clear()


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








