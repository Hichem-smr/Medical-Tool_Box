# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Normal_result.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import file_rc

class Ui_Left_Breast(object):
    def setupUi(self, Left_Breast):
        if not Left_Breast.objectName():
            Left_Breast.setObjectName(u"Left_Breast")
        Left_Breast.resize(361, 125)
        self.frame_2 = QFrame(Left_Breast)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(100, 20, 161, 21))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 67, 17))
        self.label.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.DecisionVar = QLabel(self.frame_2)
        self.DecisionVar.setObjectName(u"DecisionVar")
        self.DecisionVar.setGeometry(QRect(80, 0, 75, 18))
        self.DecisionVar.setStyleSheet(u"QLabel{\n"
"color:rgb(0, 255, 0);\n"
"border:0px;\n"
"}\n"
"")
        self.horizontalLayoutWidget = QWidget(Left_Breast)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 40, 301, 82))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Save = QPushButton(self.horizontalLayoutWidget)
        self.Save.setObjectName(u"Save")
        self.Save.setMinimumSize(QSize(0, 50))
        self.Save.setMaximumSize(QSize(234, 50))
        self.Save.setCursor(QCursor(Qt.PointingHandCursor))
        self.Save.setLayoutDirection(Qt.LeftToRight)
        self.Save.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"	color:#fff;\n"
"	border:0px;\n"
"	border-radius:20px;\n"
"	font-size:15px;\n"
"	cursor: pointer;\n"
"	background-color:#538fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        icon = QIcon()
        icon.addFile(u"assets/img/FAB-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save.setIcon(icon)
        self.Save.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.Save)

        self.Load = QPushButton(self.horizontalLayoutWidget)
        self.Load.setObjectName(u"Load")
        self.Load.setMinimumSize(QSize(0, 50))
        self.Load.setMaximumSize(QSize(234, 50))
        self.Load.setCursor(QCursor(Qt.PointingHandCursor))
        self.Load.setLayoutDirection(Qt.LeftToRight)
        self.Load.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"	color:#fff;\n"
"	border:0px;\n"
"	border-radius:20px;\n"
"	font-size:15px;\n"
"	cursor: pointer;\n"
"	background-color:#538fff;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assets/img/path395.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Load.setIcon(icon1)
        self.Load.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.Load)


        self.retranslateUi(Left_Breast)

        QMetaObject.connectSlotsByName(Left_Breast)
    # setupUi

    def retranslateUi(self, Left_Breast):
        Left_Breast.setWindowTitle(QCoreApplication.translate("Left_Breast", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Left_Breast", u"Result :", None))
        self.DecisionVar.setText(QCoreApplication.translate("Left_Breast", u"Normal \u2698", None))
        self.Save.setText(QCoreApplication.translate("Left_Breast", u"Save", None))
        self.Load.setText(QCoreApplication.translate("Left_Breast", u"Load", None))
    # retranslateUi

