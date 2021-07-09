# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MLO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import file_rc

class Ui_MLO(object):
    def setupUi(self, MLO):
        if not MLO.objectName():
            MLO.setObjectName(u"MLO")
        MLO.resize(660, 506)
        MLO.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"border:0px;\n"
"}")
        self.centralwidget = QWidget(MLO)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 641, 451))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.CCImages = QPushButton(self.layoutWidget)
        self.CCImages.setObjectName(u"CCImages")

        self.gridLayout.addWidget(self.CCImages, 0, 0, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LeftImage = QLabel(self.layoutWidget)
        self.LeftImage.setObjectName(u"LeftImage")
        self.LeftImage.setScaledContents(True)

        self.horizontalLayout.addWidget(self.LeftImage)

        self.RightImage = QLabel(self.layoutWidget)
        self.RightImage.setObjectName(u"RightImage")
        self.RightImage.setScaledContents(True)

        self.horizontalLayout.addWidget(self.RightImage)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.Import = QPushButton(self.layoutWidget)
        self.Import.setObjectName(u"Import")
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

        self.gridLayout.addWidget(self.Import, 2, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(5, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.Next = QPushButton(self.layoutWidget)
        self.Next.setObjectName(u"Next")
        self.Next.setEnabled(False)
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

        self.gridLayout.addWidget(self.Next, 2, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 5, 1, 1)

        MLO.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MLO)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 660, 22))
        MLO.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MLO)
        self.statusbar.setObjectName(u"statusbar")
        MLO.setStatusBar(self.statusbar)

        self.retranslateUi(MLO)

        QMetaObject.connectSlotsByName(MLO)
    # setupUi

    def retranslateUi(self, MLO):
        MLO.setWindowTitle(QCoreApplication.translate("MLO", u"MainWindow", None))
        self.CCImages.setText(QCoreApplication.translate("MLO", u"CC IMAGES", None))
        self.LeftImage.setText("")
        self.RightImage.setText("")
        self.Import.setText(QCoreApplication.translate("MLO", u"Import", None))
        self.Next.setText(QCoreApplication.translate("MLO", u"Next           ", None))
    # retranslateUi

