# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Filters_Decision.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(333, 626)
        self.PreviewVar = QLabel(Form)
        self.PreviewVar.setObjectName(u"PreviewVar")
        self.PreviewVar.setGeometry(QRect(10, 160, 311, 361))
        self.PreviewVar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:0px;\n"
"border:0px;\n"
"}")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 20, 130, 25))
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(180, 60, 130, 25))
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(180, 100, 130, 25))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 141, 20))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 67, 17))
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 141, 20))
        self.label_6.setStyleSheet(u"QLabel{\n"
"\n"
"color:#4b6272;\n"
"border:0px;\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}")
        self.pushButton_BtnImpostoRenda_2 = QPushButton(Form)
        self.pushButton_BtnImpostoRenda_2.setObjectName(u"pushButton_BtnImpostoRenda_2")
        self.pushButton_BtnImpostoRenda_2.setGeometry(QRect(50, 561, 234, 50))
        self.pushButton_BtnImpostoRenda_2.setMinimumSize(QSize(0, 50))
        self.pushButton_BtnImpostoRenda_2.setMaximumSize(QSize(234, 50))
        self.pushButton_BtnImpostoRenda_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_BtnImpostoRenda_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_BtnImpostoRenda_2.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u":/img/path395.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_BtnImpostoRenda_2.setIcon(icon)
        self.pushButton_BtnImpostoRenda_2.setIconSize(QSize(40, 40))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 527, 330, 30))
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

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 140, 311, 22))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget1)
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PreviewVar.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"None", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Matrix 3*3", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Matrix 5*5", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Matrix 7*7", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"None", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"Dempster Shafter", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Form", u"Yager", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Form", u"Disjunctive", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Form", u"Dubois Parade", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Form", u"PRC5", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"None", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"Optimist", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"Pessimist", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"Pignistic", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Combination rule :", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Decision :", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Filter's parametres :", None))
        self.pushButton_BtnImpostoRenda_2.setText(QCoreApplication.translate("Form", u"Result", None))
        self.LeftSwitch.setText(QCoreApplication.translate("Form", u"\u25c3", None))
        self.RightSwitch.setText(QCoreApplication.translate("Form", u"\u25b9", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Preview", None))
    # retranslateUi

