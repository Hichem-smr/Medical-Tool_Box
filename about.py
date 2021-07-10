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
        loadUi("About.ui",self)




# main
if __name__ == '__main__':
    main()