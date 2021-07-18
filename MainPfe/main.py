import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import glob
import os
from itertools import cycle
from RegionA import Pretreatement,execution,combineMLOCC
import cv2
a = 0
images = []
files = []
i = 0
n = 0

d = "a"

class Cancer(QDialog):
    def Progload(self):
        global d
        d = d +'/'
        os.chdir(d)
        print(os.getcwd())
        self.hide()
        os.system('python MainPfe/main.py')
        

    def __init__(self):
        super(Cancer, self).__init__()
        loadUi('Windows/Cancer_result.ui', self)
        self.Load.clicked.connect(self.Progload)
        self.Save.clicked.connect(self.close)

class Normal(QDialog):
    def Progload(self):
        global d
        d = d + '/'
        os.chdir(d)
        print(os.getcwd())
        self.hide()
        os.system('python MainPfe/main.py')
        

    
    def __init__(self):
        super(Normal, self).__init__()
        loadUi('Windows/Normal_result.ui', self)
        self.Load.clicked.connect(self.Progload)
        self.Save.clicked.connect(self.close)

class CancerRight(QDialog):
    def __init__(self):
        super(CancerRight, self).__init__()
        loadUi('Windows/Cancer_result1.ui', self)
        self.Next.clicked.connect(self.close)
        self.Save.clicked.connect(self.close)


class NormalRight(QDialog):
    def __init__(self):
        super(NormalRight, self).__init__()
        loadUi('Windows/Normal_result1.ui', self)
        self.Next.clicked.connect(self.close)
        self.Save.clicked.connect(self.close)

class Filters(QDialog):
    def __init__(self):
        super(Filters, self).__init__()
        loadUi('Windows/F.ui', self)
        global i
        i = 1
        self.RightSwitch.clicked.connect(self.RightImage)
        self.LeftSwitch.clicked.connect(self.LeftImage)
        self.comboBox.activated.connect(self.Filter)
        self.comboBox_2.activated.connect(self.decision)
        self.comboBox_3.activated.connect(self.Combination)
        self.result.clicked.connect(self.Process)

    def Process(self):
        global n 
        filter   = str(self.comboBox.currentText())
        regle    = str(self.comboBox_2.currentText())
        decision = str(self.comboBox_3.currentText())
        age = int(self.age.text())
        # regle : 0 conjonctive, 1 disjonctive, 2 hybride, 3 pcr, 4 yager.
        # decision : 0 bel , 1 pl, 2 pi

        if filter == "Matrix 3*3":
            f = 0
        elif filter == "Matrix 5*5":
            f = 1
        elif filter == "Matrix 7*7":
            f = 2
        
        if regle == "Dempster Shafter":
            r = 0
        elif regle == "Yager":
            r = 4
        elif regle == "Disjunctive":
            r = 1
        elif regle == "Dubois Parade":
            r = 2
        elif regle == "PRC5":
            r = 3

        if decision == "Optimist":
            d = 1
        elif decision == "Pessimist":
            d = 0
        elif decision == "Pignistic":
            d = 2

        CC_Right = execution(images[0].image, images[0].type, r, d)
        MLO_Right = execution(images[1].image, images[1].type, r, d)
        CC_Left = execution(images[2].image, images[2].type, r, d)
        MLO_Left = execution(images[3].image, images[3].type, r, d)

        # img = cv2.imread(files[0])
        # img = cv2.equalizeHist(img)
        # img1 = cv2.imread(files[1])
        # img1 = cv2.equalizeHist(img1)
        # img2 = cv2.imread(files[2])
        # img2 = cv2.equalizeHist(img2)
        # img3 = cv2.imread(files[3])
        # img3 = cv2.equalizeHist(img3)

        # print(img  = images[0].image)
        # print(img1 =images[1].image)
        # print(img2 =images[2].image)
        # print(img3 =images[3].image)

        print(MLO_Right[1])
        print(CC_Right[1])  
        print(MLO_Left[1])
        print(CC_Left[1])

        print(MLO_Right[1]['M'])
        
        result_right = combineMLOCC(MLO_Right[1], CC_Right[1], age, r, d)
        result_left  = combineMLOCC(MLO_Left[1], CC_Left[1], age, r, d)

        W_FILTERS.hide()

        # files.append(os.getcwd() + "/RIGHT_CC.jpg")
        # files.append(os.getcwd() + "/LEFT_CC.jpg")
        # files.append(os.getcwd() + "/RIGHT_MLO.jpg")
        # files.append(os.getcwd() + "/LEFT_MLO.jpg")

        print(result_right)
        print(result_left)

        if(result_right == frozenset({'M'})):
            if(MLO_Right[1]['M'] > CC_Right[1]['M']):
                url = files[2]
            else: 
                url = files[0]
                
            W_CANCER.ImageVAR.setStyleSheet("border-image : url(" + url + ");")
            W_CANCER.show()
            
        else:
            W_NORMAL.show()

        # while(W_CANCER.isVisible() or W_NORMAL.isVisible()):
        #     n = n + 1

        if(result_left == frozenset({'M'})):
            if(MLO_Left[1]['M'] > CC_Left[1]['M']):
                url = files[3]
            else: 
                url = files[1]
                
            W1_CANCER.ImageVAR.setStyleSheet("border-image : url(" + url + ");")
            W1_CANCER.show()
        else:
            W1_NORMAL.show()


    def Filter(self): 
        self.Activation()

    def decision(self):   
        self.Activation()

    def Combination(self):
      self.Activation()

    def Activation(self):
        if(str(self.comboBox.currentText()) != "None" and str(self.comboBox_2.currentText()) != "None" and str(self.comboBox_3.currentText()) != "None"):
            self.result.setEnabled(True)
        else: 
            self.result.setEnabled(False)

    def RightImage(self):
        self.PreviewVar.setStyleSheet("border-image : url(" + self.NextIm() + ");")
    
    def LeftImage(self):
        self.PreviewVar.setStyleSheet("border-image : url(" + self.PrevIm() + ");")

    def NextIm(self):
        global i 
        if(i < len(files) - 1):
            i = i + 1
        else: i = 0
        return files[i]

    def PrevIm(self):
        global i 
        if(i < 1):
            i = len(files) - 1
        else: i = i - 1
        print(images[i].type)
        return files[i]


class Save(QDialog):
    def __init__(self):
        super(Save,self).__init__()
        loadUi("Windows/Import_Images_CC.ui",self)
        self.RightImport.clicked.connect(self.browsefilesRight)
        self.LeftImport.clicked.connect(self.browsefilesLeft)
        self.ValidateVar.clicked.connect(self.NextActivate)
        self.CancelVar.clicked.connect(self.close)
        

        
        ##Esc poses a problem, path gets removed and validate is active
 
    def browsefilesRight(self):
        global a
        fname=QFileDialog.getOpenFileName(self, 'Open file', '/home/hichemhero/Desktop/pyds/opencv/MainPfe', 'Images (*.png, *.xmp *.jpg)')
        self.RightPathPreview.setText(fname[0])
        self.Activation()


    def browsefilesLeft(self):
        global a
        fname=QFileDialog.getOpenFileName(self, 'Open file', '/home/hichemhero/Desktop/pyds/opencv/MainPfe', 'Images (*.png, *.xmp *.jpg)')
        self.LeftPathPreview.setText(fname[0])
        self.Activation()
        
    def Activation(self):
        global a
        if self.RightPathPreview.toPlainText() != "" and self.LeftPathPreview.toPlainText() != "" :
            self.ValidateVar.setEnabled(True)
            
        else: 
            self.ValidateVar.setEnabled(False)
    
    def NextActivate(self):
        self.ImageLoad()
        if(W_LOAD_CC.ValidateVar.isEnabled() and W_LOAD_MLO.ValidateVar.isEnabled()):
            CC_WINDOW.Next.setEnabled(True)
            MLO_WINDOW.Next.setEnabled(True)
        else:
            CC_WINDOW.Next.setEnabled(False)
            MLO_WINDOW.Next.setEnabled(False)
        self.hide()
    
    def ImageLoad(self):
        b = self.RightPathPreview.toPlainText()
        c = self.LeftPathPreview.toPlainText()
        
        if(self == W_LOAD_CC):
            CC_WINDOW.RightImage.setStyleSheet("border-image : url(" + b + ");")
            CC_WINDOW.LeftImage.setStyleSheet("border-image : url(" + c + ");")
        else:
            MLO_WINDOW.RightImage.setStyleSheet("border-image : url(" + b + ");")
            MLO_WINDOW.LeftImage.setStyleSheet("border-image : url(" + c + ");")

class ImageInfo():
    def __init__(self, url, type, ):
        self.url = "Temp/" +url
        #check if this imread is working
        self.image = cv2.imread(url, 0)
        self.type = type


class MainCC(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainCC, self).__init__()
        loadUi('Windows/CC.ui', self)
        self.Import.clicked.connect(self.ImportImagesCC)
        self.MLOSwitch.clicked.connect(self.Switch)
        self.Next.clicked.connect(self.NextSwitch)
        
        
    def Switch(self):
        CC_WINDOW.hide()
        MLO_WINDOW.show()

    def ImportImagesCC(self):
        W_LOAD_CC.show()

    def NextSwitch(self):
        global files,images
        
        Right_CC = ImageInfo(W_LOAD_CC.RightPathPreview.toPlainText(), "RIGHT_CC")
        Left_CC = ImageInfo(W_LOAD_CC.LeftPathPreview.toPlainText(), "LEFT_CC")
        Right_MLO = ImageInfo(W_LOAD_MLO.RightPathPreview.toPlainText(),"RIGHT_MLO")
        Left_MLO = ImageInfo(W_LOAD_MLO.LeftPathPreview.toPlainText(), "LEFT_MLO")

        #check if these images are loading
        Right_CC.image = Pretreatement(Right_CC.image, Right_CC.type)
        Left_CC.image = Pretreatement(Left_CC.image, Left_CC.type)
        Right_MLO.image = Pretreatement(Right_MLO.image, Right_MLO.type)
        Left_MLO.image = Pretreatement(Left_MLO.image, Left_MLO.type)

        files.append(os.getcwd() + "/Temp/RIGHT_CC.jpg")
        files.append(os.getcwd() + "/Temp/RIGHT_MLO.jpg")
        files.append(os.getcwd() + "/Temp/LEFT_CC.jpg")
        files.append(os.getcwd() + "/Temp/LEFT_MLO.jpg")

        images.append(Right_CC)
        images.append(Right_MLO)
        images.append(Left_CC)
        images.append(Left_MLO)

        #border image works with url, need to find a way to put images[0] directly without url
        W_FILTERS.PreviewVar.setStyleSheet("border-image : url(" + files[0] + ");")
        CC_WINDOW.hide()
        W_FILTERS.show()


class MainMLO(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainMLO, self).__init__()
        loadUi('Windows/MLO.ui', self)
        self.Import.clicked.connect(self.ImportImagesMLO)
        self.CCImages.clicked.connect(self.Switch)
        self.Next.clicked.connect(self.NextSwitch)

    def Switch(self):
        MLO_WINDOW.hide()
        CC_WINDOW.show()

    def ImportImagesMLO(self):
        W_LOAD_MLO.show()

    def NextSwitch(self):
        global files,images
        
        Right_CC = ImageInfo(W_LOAD_CC.RightPathPreview.toPlainText(), "RIGHT_CC")
        Left_CC = ImageInfo(W_LOAD_CC.LeftPathPreview.toPlainText(), "LEFT_CC")
        Right_MLO = ImageInfo(W_LOAD_MLO.RightPathPreview.toPlainText(),"RIGHT_MLO")
        Left_MLO = ImageInfo(W_LOAD_MLO.LeftPathPreview.toPlainText(), "LEFT_MLO")
        
        #check if these images are loading
        Right_CC.image = Pretreatement(Right_CC.image, Right_CC.type)
        Left_CC.image = Pretreatement(Left_CC.image, Left_CC.type)
        Right_MLO.image = Pretreatement(Right_MLO.image, Right_MLO.type)
        Left_MLO.image = Pretreatement(Left_MLO.image, Left_MLO.type)

        images.append(Right_CC)
        images.append(Right_MLO)
        images.append(Left_CC)
        images.append(Left_MLO)

        files.append(os.getcwd() + "/Temp/RIGHT_CC.jpg")
        files.append(os.getcwd() + "/Temp/RIGHT_MLO.jpg")
        files.append(os.getcwd() + "/Temp/LEFT_CC.jpg")
        files.append(os.getcwd() + "/Temp/LEFT_MLO.jpg")
        print(files[0])

        #border image works with url, need to find a way to put images[0] directly without url
        W_FILTERS.PreviewVar.setStyleSheet("border-image : url(" + files[0] + ");")
        MLO_WINDOW.hide()
        W_FILTERS.show()

d = os.getcwd() 
os.chdir(os.getcwd() + "/" + "MainPfe/")
print(os.getcwd())
app = QtWidgets.QApplication(sys.argv)

CC_WINDOW = MainCC()
W_LOAD_CC = Save()
MLO_WINDOW = MainMLO()
W_LOAD_MLO = Save()
W_FILTERS = Filters()
W1_CANCER = CancerRight()
W1_NORMAL = NormalRight()
W_CANCER = Cancer()
W_NORMAL = Normal()

CC_WINDOW.show()
# W_FILTERS.show()
app.exec_()

