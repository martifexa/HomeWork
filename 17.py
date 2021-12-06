
import sys
import csv
from tablitsa import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lst = []
        self.loadTable('rez.csv')
        school = []
        classes = []
        for i in self.lst:
            school.append(i[0])
            classes.append(i[1])
        school = sorted(list(set(school)))
        classes = sorted(list(set(classes)))
        school.insert(0, 'Все')
        classes.insert(0, 'Все')
        self.comboBox.insertItems(0, school)
        self.comboBox_2.insertItems(0, classes)
        for i in range(len(self.reader)):
            self.lst[i].append(self.reader[i][1])
        self.pushButton.clicked.connect(self.results)
        self.comboBox.currentTextChanged.connect(self.combo)

    def loadTable(self, table_name):
            with open(table_name, encoding="utf8") as csvfile:
                self.reader = list(csv.reader(csvfile,
                                              delimiter=',', quotechar='"'))
                self.tableWidget.setColumnCount(3)
                self.tableWidget.setHorizontalHeaderLabels(['Фамилия','Результат','Логин'])
                #print(self.reader)
                del self.reader[0]
                self.reader = list(map(lambda x: [x[1], x[7], x[1]], self.reader))
                self.lst = list(map(lambda x: x[0].split(' '), self.reader))
                self.lst = list(map(lambda x: [x[1], x[2], x[3]], self.lst))
                #print(self.lst)
                self.reader = list(map(lambda x: [x[0][8:-2], x[1], x[2]], self.reader))
                #print(self.reader)
                for i, row in enumerate(self.reader):
                    self.tableWidget.setRowCount(
                        self.tableWidget.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.tableWidget.setItem(
                            i, j, QTableWidgetItem(elem))
                # print(self.reader)
                self.tableWidget.resizeColumnsToContents()


    def combo(self, text):
        if text == 'Все':
            return
        new_combo = []
        for i in range(len(self.lst)):
            if self.lst[i][0] == text:
                new_combo.append(self.lst[i][1])
        new_combo = sorted(list(set(new_combo)))
        self.comboBox_2.clear()
        self.comboBox_2.insertItem(0, 'Все')
        self.comboBox_2.addItems(new_combo)

    def results(self):
        self.tableWidget.setRowCount(0)
        res = []
        win = []

        for j in range(len(self.lst)):
            if self.comboBox.currentText() == 'Все':
                if self.lst[j][1] == self.comboBox_2.currentText():
                    res.append([self.lst[j][2], self.lst[j][3], self.reader[j][2]])
                    win.append(self.lst[j][3])
        win = list(map(lambda x: int(x), win))
        win = sorted(list(set(win)), reverse=True)[:3]
        #print(win)
        for j in range(len(self.lst)):
            if self.comboBox_2.currentText() == 'Все':
                if self.lst[j][0] == self.comboBox.currentText():
                    res.append([self.lst[j][2], self.lst[j][3], self.reader[j][2]])
                    win.append(self.lst[j][3])
        win = list(map(lambda x: int(x), win))
        win = sorted(list(set(win)), reverse=True)[:3]

        #print(win)

        for i in range(len(self.lst)):
            if self.lst[i][0] == self.comboBox.currentText() and self.lst[i][1] == self.comboBox_2.currentText():
                res.append([self.lst[i][2], self.lst[i][3], self.reader[i][2]])
                win.append(self.lst[i][3])
        win = list(map(lambda x: int(x), win))
        win = sorted(list(set(win)), reverse=True)[:3]

        #print(win)
        for i in range(len(self.lst)):

            if self.comboBox.currentText() == 'Все' and self.comboBox_2.currentText() == 'Все':
                res.append([self.lst[i][2], self.lst[i][3], self.reader[i][2]])
                win.append(self.lst[i][3])
        win = list(map(lambda x: int(x), win))
        win = sorted(list(set(win)), reverse=True)[:3]
        print(res)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))



        for i, row in enumerate(res):
            for y in range(len(row)):
                if int(res[i][1]) == win[0]:
                    self.tableWidget.item(i, y).setBackground(QColor('yellow'))
                elif int(res[i][1]) == win[1]:
                    self.tableWidget.item(i, y).setBackground(QColor('grey'))
                elif int(res[i][1]) == win[2]:
                    self.tableWidget.item(i, y).setBackground(QColor('brown'))

        #print(win)



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