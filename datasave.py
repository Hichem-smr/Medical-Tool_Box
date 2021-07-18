import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
import json
Desc = ""
url = ""

def main():
    app = QApplication(sys.argv)


    saved = MainDataSet()
    saved.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

class MainDataSet(QMainWindow):
    def __init__(self):
        global Desc, url
        super(MainDataSet, self).__init__()
        loadUi("addlist.ui",self)
        self.ValidateVar.clicked.connect(self.save)


    
    def save(self):
        global Desc, url

        Desc = str(self.Desc.text())
        url = str(self.url.text())

        f = open('Dataset/outputfile',)
        people = json.load(f)   

        element={"name":Desc,"address":url}
        people.append(element)
        
        with open('Dataset/outputfile', 'w') as fout:
            json.dump(people, fout)

        self.close()
        


if __name__ == '__main__':
    main()


# main
