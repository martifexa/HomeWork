import fileinput
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ten import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        try:
            file = open(self.lineEdit.text(), 'r', encoding="utf-8")

        except IOError as e:
            self.textBrowser.setText(f'Файл {self.lineEdit.text()} не найден')
        else:
            with file:
                lst = file.readline().split(' ')
                lst1 = []
                try:
                    for i in lst:
                        lst1.append(int(i))
                    self.lineEdit_2.setText(f'{min(lst1)}')
                    self.lineEdit_3.setText(f'{max(lst1)}')
                    self.lineEdit_4.setText(f'{sum(lst1) / len(lst1)}')
                except ValueError or TypeError:
                    self.textBrowser.setText(f'Ты дебил')





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

