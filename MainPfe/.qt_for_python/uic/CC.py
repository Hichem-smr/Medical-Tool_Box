# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import file_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 506)
        MainWindow.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"border:0px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 640, 361))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftImage = QLabel(self.horizontalLayoutWidget)
        self.LeftImage.setObjectName(u"LeftImage")
        self.LeftImage.setScaledContents(True)

        self.horizontalLayout.addWidget(self.LeftImage)

        self.RightImage = QLabel(self.horizontalLayoutWidget)
        self.RightImage.setObjectName(u"RightImage")
        self.RightImage.setScaledContents(True)

        self.horizontalLayout.addWidget(self.RightImage)

        self.MLOSwitch = QPushButton(self.centralwidget)
        self.MLOSwitch.setObjectName(u"MLOSwitch")
        self.MLOSwitch.setGeometry(QRect(10, 30, 120, 20))
        self.Import = QPushButton(self.centralwidget)
        self.Import.setObjectName(u"Import")
        self.Import.setGeometry(QRect(90, 410, 151, 50))
        self.Import.setMinimumSize(QSize(0, 50))
        self.Import.setMaximumSize(QSize(234, 50))
        self.Import.setCursor(QCursor(Qt.PointingHandCursor))
        self.Import.setLayoutDirection(Qt.LeftToRight)
        self.Import.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"	color:#fff;\n"
"	border:0px;\n"
"	border-radius:10px;\n"
"	font-size:15px;\n"
"	cursor: pointer;\n"
"	background-color:#538fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        icon = QIcon()
        icon.addFile(u"assets/img/FAB-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Import.setIcon(icon)
        self.Import.setIconSize(QSize(40, 40))
        self.Next = QPushButton(self.centralwidget)
        self.Next.setObjectName(u"Next")
        self.Next.setEnabled(False)
        self.Next.setGeometry(QRect(420, 410, 160, 50))
        self.Next.setMinimumSize(QSize(0, 50))
        self.Next.setMaximumSize(QSize(234, 50))
        self.Next.setCursor(QCursor(Qt.PointingHandCursor))
        self.Next.setLayoutDirection(Qt.LeftToRight)
        self.Next.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"	color:#fff;\n"
"	border:0px;\n"
"	border-radius:10px;\n"
"	font-size:15px;\n"
"	cursor: pointer;\n"
"	background-color:#538fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assets/img/path395.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Next.setIcon(icon1)
        self.Next.setIconSize(QSize(40, 40))
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
        self.LeftImage.setText("")
        self.RightImage.setText("")
        self.MLOSwitch.setText(QCoreApplication.translate("MainWindow", u"MLO IMAGES", None))
        self.Import.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.Next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

