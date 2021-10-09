import sys
from mac import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.zakaz)


    def zakaz(self):
        self.plainTextEdit.setPlainText('Ваш заказ:')
        if self.checkBox_1.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_1.text())
        if self.checkBox_2.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_2.text())
        if self.checkBox_3.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_3.text())
        if self.checkBox_4.isChecked():
            self.plainTextEdit.appendPlainText(self.checkBox_4.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


