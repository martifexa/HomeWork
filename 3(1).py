import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class Arifm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 360, 150)
        self.setWindowTitle('Арифмометр')

        self.vvod1 = QLineEdit(self)
        self.vvod1.setGeometry(100, 20, 50, 30)

        self.plus = QPushButton(self)
        self.plus.setText('+')
        self.plus.setGeometry(150, 20, 30, 30)
        self.plus.clicked.connect(self.sum)

        self.minus = QPushButton(self)
        self.minus.setText('-')
        self.minus.setGeometry(180, 20, 30, 30)
        self.minus.clicked.connect(self.chastnoe)

        self.multiply = QPushButton(self)
        self.multiply.setText('*')
        self.multiply.setGeometry(210, 20, 30, 30)
        self.multiply.clicked.connect(self.proisved)

        self.vvod2 = QLineEdit(self)
        self.vvod2.setGeometry(240, 20, 50, 30)

        self.equally = QLineEdit(self)
        self.equally.setGeometry(290, 20, 50, 30)
        self.equally.setReadOnly(True)


    def sum(self):
        self.equally.setText(str(float(self.vvod1.text()) + float(self.vvod2.text())))

    def chastnoe(self):
        self.equally.setText(str(float(self.vvod1.text()) - float(self.vvod2.text())))

    def proisved(self):
        self.equally.setText(str(float(self.vvod1.text()) * float(self.vvod2.text())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifm()
    ex.show()
    sys.exit(app.exec())


