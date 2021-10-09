

import sys

# Импортируем из PyQt5.QtWidgets классы для создания приложения и виджета

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel, QLCDNumber


# Унаследуем наш класс от простейшего графического примитива QWidget
class Foc(QWidget):
    def __init__(self):
        # Надо не забыть вызвать инициализатор базового класса
        super().__init__()



        # Зададим размер и положение нашего виджета,
        self.setGeometry(300, 300, 320, 60)
        # А также его заголовок
        self.setWindowTitle('Фокус со словами')

        self.btn = QPushButton(self)
        self.btn.setText("->")
        self.btn.setGeometry(140, 20, 30, 30)
        self.btn.clicked.connect(self.word)
        self.right = QLineEdit(self)
        self.right.setGeometry(175, 20, 125, 30)

        self.left = QLineEdit(self)

        self.left.setGeometry(10, 20, 125, 30)

    def word(self):
        if self.btn.text() == '->':
            self.btn.setText('<-')
            self.right.setText(self.left.text())
            self.left.setText(' ')

        else:
            self.btn.setText('->')
            self.left.setText(self.right.text())
            self.right.setText(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Foc()
    ex.show()
    sys.exit(app.exec())






