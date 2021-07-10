# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CC_with bottoms.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 506)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 331, 361))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Images = QLabel(self.horizontalLayoutWidget)
        self.Images.setObjectName(u"Images")

        self.horizontalLayout.addWidget(self.Images)

        self.MLOImages = QPushButton(self.centralwidget)
        self.MLOImages.setObjectName(u"MLOImages")
        self.MLOImages.setGeometry(QRect(10, 30, 120, 20))
        self.NextVar = QPushButton(self.centralwidget)
        self.NextVar.setObjectName(u"NextVar")
        self.NextVar.setEnabled(False)
        self.NextVar.setGeometry(QRect(390, 410, 161, 51))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(380, 200, 168, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftSwitch = QPushButton(self.horizontalLayoutWidget_2)
        self.LeftSwitch.setObjectName(u"LeftSwitch")
        self.LeftSwitch.setEnabled(True)
        self.LeftSwitch.setTabletTracking(False)

        self.horizontalLayout_2.addWidget(self.LeftSwitch)

        self.RightSwitch = QPushButton(self.horizontalLayoutWidget_2)
        self.RightSwitch.setObjectName(u"RightSwitch")

        self.horizontalLayout_2.addWidget(self.RightSwitch)

        self.ImportVar = QPushButton(self.centralwidget)
        self.ImportVar.setObjectName(u"ImportVar")
        self.ImportVar.setEnabled(True)
        self.ImportVar.setGeometry(QRect(90, 410, 161, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 657, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Images.setText("")
        self.MLOImages.setText(QCoreApplication.translate("MainWindow", u"MLO IMAGES", None))
        self.NextVar.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.LeftSwitch.setText(QCoreApplication.translate("MainWindow", u"\u25c3", None))
        self.RightSwitch.setText(QCoreApplication.translate("MainWindow", u"\u25b9", None))
        self.ImportVar.setText(QCoreApplication.translate("MainWindow", u"Import", None))
    # retranslateUi

