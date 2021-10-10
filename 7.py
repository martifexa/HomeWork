import sys
from McDonalds import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.zakaz)
        self.checkBox_1.clicked.connect(self.edin)
        self.checkBox_2.clicked.connect(self.edin)
        self.checkBox_3.clicked.connect(self.edin)
        self.checkBox_4.clicked.connect(self.edin)

    def edin(self):
        if self.checkBox_1.isChecked():
            self.lineEdit.setText('1')
        if self.checkBox_2.isChecked():
            self.lineEdit_2.setText('1')
        if self.checkBox_3.isChecked():
            self.lineEdit_3.setText('1')
        if self.checkBox_4.isChecked():
            self.lineEdit_4.setText('1')

    def zakaz(self):
        self.plainTextEdit.setPlainText('Ваш заказ:')
        self.plainTextEdit.appendPlainText('')
        if self.checkBox_1.isChecked():
            self.plainTextEdit.appendPlainText(f' {self.checkBox_1.text()}-----{self.lineEdit.text()}-----{int(self.lineEdit.text()) * 50}')
        if self.checkBox_2.isChecked():
            self.plainTextEdit.appendPlainText(f' {self.checkBox_2.text()}-----{self.lineEdit_2.text()}-----{int(self.lineEdit_2.text()) * 70}')
        if self.checkBox_3.isChecked():
            self.plainTextEdit.appendPlainText(f' {self.checkBox_3.text()}-----{self.lineEdit_3.text()}-----{int(self.lineEdit_3.text()) * 60}')
        if self.checkBox_4.isChecked():
            self.plainTextEdit.appendPlainText(f' {self.checkBox_4.text()}-----{self.lineEdit_4.text()}-----{int(self.lineEdit_4.text()) * 40}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())