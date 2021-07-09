import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
import json

def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("tableslist.ui",self)
        self.tableWidget.setColumnWidth(0,310)
        self.tableWidget.setColumnWidth(1,580)
        self.loaddata()

    def loaddata(self):
        f = open('Dicti/outputfile',)
        people = json.load(f)   

        row=0
        self.tableWidget.setRowCount(len(people))
        for person in people:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(person["name"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(person["address"]))
            row=row+1



# main
if __name__ == '__main__':
    main()