# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'F.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import file_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(329, 663)
        self.comboBox_3 = QComboBox(Dialog)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(180, 130, 130, 25))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 557, 330, 30))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LeftSwitch = QPushButton(self.layoutWidget)
        self.LeftSwitch.setObjectName(u"LeftSwitch")
        self.LeftSwitch.setEnabled(True)
        self.LeftSwitch.setTabletTracking(False)

        self.horizontalLayout_2.addWidget(self.LeftSwitch)

        self.RightSwitch = QPushButton(self.layoutWidget)
        self.RightSwitch.setObjectName(u"RightSwitch")

        self.horizontalLayout_2.addWidget(self.RightSwitch)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(33, 90, 141, 20))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 50, 151, 20))
        self.label_6.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(95, 130, 71, 17))
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 50, 130, 25))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(180, 90, 130, 25))
        self.PreviewVar = QLabel(Dialog)
        self.PreviewVar.setObjectName(u"PreviewVar")
        self.PreviewVar.setGeometry(QRect(10, 189, 311, 361))
        self.PreviewVar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:0px;\n"
"border:0px;\n"
"}")
        self.result = QPushButton(Dialog)
        self.result.setObjectName(u"result")
        self.result.setEnabled(False)
        self.result.setGeometry(QRect(50, 590, 234, 50))
        self.result.setMinimumSize(QSize(0, 50))
        self.result.setMaximumSize(QSize(234, 50))
        self.result.setCursor(QCursor(Qt.PointingHandCursor))
        self.result.setLayoutDirection(Qt.LeftToRight)
        self.result.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u"assets/img/path395.png", QSize(), QIcon.Normal, QIcon.Off)
        self.result.setIcon(icon)
        self.result.setIconSize(QSize(40, 40))
        self.layoutWidget_2 = QWidget(Dialog)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 169, 311, 22))
        self.gridLayout = QGridLayout(self.layoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 20, 67, 17))
        self.label_7.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.age = QLineEdit(Dialog)
        self.age.setObjectName(u"age")
        self.age.setGeometry(QRect(180, 20, 61, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Dialog", u"Optimist", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Dialog", u"Pessimist", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Dialog", u"Pignistic", None))

        self.LeftSwitch.setText(QCoreApplication.translate("Dialog", u"\u25c3", None))
        self.RightSwitch.setText(QCoreApplication.translate("Dialog", u"\u25b9", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Combination rule :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Filter's parametres :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Decision :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Matrix 3*3", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Matrix 5*5", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Matrix 7*7", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Dempster Shafter", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Dialog", u"Yager", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Dialog", u"Disjunctive", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Dialog", u"Dubois Parade", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Dialog", u"PRC5", None))

        self.PreviewVar.setText("")
        self.result.setText(QCoreApplication.translate("Dialog", u"Result", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Age :", None))
    # retranslateUi

