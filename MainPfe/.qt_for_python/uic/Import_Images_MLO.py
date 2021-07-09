# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Import_Images_MLO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(645, 206)
        self.RightImport = QPushButton(Form)
        self.RightImport.setObjectName(u"RightImport")
        self.RightImport.setGeometry(QRect(500, 40, 89, 30))
        self.ValidateVar = QPushButton(Form)
        self.ValidateVar.setObjectName(u"ValidateVar")
        self.ValidateVar.setEnabled(False)
        self.ValidateVar.setGeometry(QRect(340, 160, 89, 25))
        self.RightPathPreview = QTextBrowser(Form)
        self.RightPathPreview.setObjectName(u"RightPathPreview")
        self.RightPathPreview.setGeometry(QRect(30, 40, 460, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 201, 17))
        self.LeftImport = QPushButton(Form)
        self.LeftImport.setObjectName(u"LeftImport")
        self.LeftImport.setGeometry(QRect(500, 100, 89, 30))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 201, 17))
        self.LeftPathPreview = QTextBrowser(Form)
        self.LeftPathPreview.setObjectName(u"LeftPathPreview")
        self.LeftPathPreview.setGeometry(QRect(30, 100, 460, 31))
        self.CancelVar = QPushButton(Form)
        self.CancelVar.setObjectName(u"CancelVar")
        self.CancelVar.setGeometry(QRect(210, 160, 89, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.RightImport.setText(QCoreApplication.translate("Form", u"Choose", None))
        self.ValidateVar.setText(QCoreApplication.translate("Form", u"Validate", None))
        self.RightPathPreview.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Right MLO  Image", None))
        self.LeftImport.setText(QCoreApplication.translate("Form", u"Choose", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Left MLO  Image", None))
        self.CancelVar.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

