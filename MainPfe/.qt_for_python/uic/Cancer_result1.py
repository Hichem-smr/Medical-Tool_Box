# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cancer_result1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import file_rc

class Ui_Right_Breast(object):
    def setupUi(self, Right_Breast):
        if not Right_Breast.objectName():
            Right_Breast.setObjectName(u"Right_Breast")
        Right_Breast.resize(365, 505)
        self.frame_2 = QFrame(Right_Breast)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(103, 10, 160, 18))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 67, 17))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.DecisionVar_2 = QLabel(self.frame_2)
        self.DecisionVar_2.setObjectName(u"DecisionVar_2")
        self.DecisionVar_2.setGeometry(QRect(80, 0, 75, 18))
        self.DecisionVar_2.setStyleSheet(u"QLabel{\n"
"color:rgb(255, 0, 0);\n"
"border:0px;\n"
"}\n"
"")
        self.frame = QFrame(Right_Breast)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 40, 330, 391))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 0, 67, 17))
        self.label_5.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.ImageVAR = QLabel(self.frame)
        self.ImageVAR.setObjectName(u"ImageVAR")
        self.ImageVAR.setGeometry(QRect(0, 18, 331, 371))
        self.ImageVAR.setStyleSheet(u"QLabel{\n"
"color:#4b6272;\n"
"border:0px;\n"
"}\n"
"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"border:0px;\n"
"}")
        self.horizontalLayoutWidget = QWidget(Right_Breast)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 430, 330, 82))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_2.addWidget(self.Save)

        self.Next = QPushButton(self.horizontalLayoutWidget)
        self.Next.setObjectName(u"Next")
        self.Next.setMinimumSize(QSize(0, 50))
        self.Next.setMaximumSize(QSize(234, 50))
        self.Next.setCursor(QCursor(Qt.PointingHandCursor))
        self.Next.setLayoutDirection(Qt.LeftToRight)
        self.Next.setStyleSheet(u"QPushButton{\n"
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
        self.Next.setIcon(icon1)
        self.Next.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.Next)


        self.retranslateUi(Right_Breast)

        QMetaObject.connectSlotsByName(Right_Breast)
    # setupUi

    def retranslateUi(self, Right_Breast):
        Right_Breast.setWindowTitle(QCoreApplication.translate("Right_Breast", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Right_Breast", u"Result :", None))
        self.DecisionVar_2.setText(QCoreApplication.translate("Right_Breast", u"Cancer \u2620", None))
        self.label_5.setText(QCoreApplication.translate("Right_Breast", u"Preview", None))
        self.ImageVAR.setText("")
        self.Save.setText(QCoreApplication.translate("Right_Breast", u"Save", None))
        self.Next.setText(QCoreApplication.translate("Right_Breast", u"Next", None))
    # retranslateUi

