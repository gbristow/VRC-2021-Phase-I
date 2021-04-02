# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startup_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_RCC_startup(object):
    def setupUi(self, RCC_startup):
        if not RCC_startup.objectName():
            RCC_startup.setObjectName(u"RCC_startup")
        RCC_startup.resize(234, 210)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RCC_startup.sizePolicy().hasHeightForWidth())
        RCC_startup.setSizePolicy(sizePolicy)
        RCC_startup.setMinimumSize(QSize(234, 210))
        RCC_startup.setMaximumSize(QSize(234, 210))
        RCC_startup.setStyleSheet(u"background-color: rgb(121, 121, 121);")
        self.formLayout = QFormLayout(RCC_startup)
        self.formLayout.setObjectName(u"formLayout")
        self.Title = QLabel(RCC_startup)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Title.setFont(font)
        self.Title.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"background-color: rgba(86, 81, 100, 200);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;")
        self.Title.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.Title)

        self.COM_Port_Label = QLabel(RCC_startup)
        self.COM_Port_Label.setObjectName(u"COM_Port_Label")
        self.COM_Port_Label.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 3px;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.COM_Port_Label)

        self.COM_Port_comboBox = QComboBox(RCC_startup)
        self.COM_Port_comboBox.setObjectName(u"COM_Port_comboBox")
        self.COM_Port_comboBox.setStyleSheet(u"font: 12pt \"Arial Narrow\";\n"
"background-color: rgb(235, 235, 235);")
        self.COM_Port_comboBox.setMaxCount(10)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.COM_Port_comboBox)

        self.Baud_Rate_Label = QLabel(RCC_startup)
        self.Baud_Rate_Label.setObjectName(u"Baud_Rate_Label")
        self.Baud_Rate_Label.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 3px;\n"
"")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.Baud_Rate_Label)

        self.Baud_Rate_comboBox = QComboBox(RCC_startup)
        self.Baud_Rate_comboBox.addItem("")
        self.Baud_Rate_comboBox.addItem("")
        self.Baud_Rate_comboBox.addItem("")
        self.Baud_Rate_comboBox.addItem("")
        self.Baud_Rate_comboBox.addItem("")
        self.Baud_Rate_comboBox.addItem("")
        self.Baud_Rate_comboBox.addItem("")
        self.Baud_Rate_comboBox.setObjectName(u"Baud_Rate_comboBox")
        self.Baud_Rate_comboBox.setAutoFillBackground(False)
        self.Baud_Rate_comboBox.setStyleSheet(u"font: 12pt \"Arial Narrow\";\n"
"background-color: rgb(235, 235, 235);")
        self.Baud_Rate_comboBox.setMaxCount(10)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.Baud_Rate_comboBox)

        self.Connect_Button = QPushButton(RCC_startup)
        self.Connect_Button.setObjectName(u"Connect_Button")
        self.Connect_Button.setMinimumSize(QSize(0, 35))
        self.Connect_Button.setAutoFillBackground(True)
        self.Connect_Button.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(255, 85, 0);\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"")
        self.Connect_Button.setCheckable(True)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.Connect_Button)


        self.retranslateUi(RCC_startup)

        QMetaObject.connectSlotsByName(RCC_startup)
    # setupUi

    def retranslateUi(self, RCC_startup):
        RCC_startup.setWindowTitle(QCoreApplication.translate("RCC_startup", u"Form", None))
        self.Title.setText(QCoreApplication.translate("RCC_startup", u"RCC ADU Connect", None))
        self.COM_Port_Label.setText(QCoreApplication.translate("RCC_startup", u"COM Port", None))
        self.COM_Port_comboBox.setCurrentText("")
        self.Baud_Rate_Label.setText(QCoreApplication.translate("RCC_startup", u"Baud Rate", None))
        self.Baud_Rate_comboBox.setItemText(0, QCoreApplication.translate("RCC_startup", u"1000000", None))
        self.Baud_Rate_comboBox.setItemText(1, QCoreApplication.translate("RCC_startup", u"460800", None))
        self.Baud_Rate_comboBox.setItemText(2, QCoreApplication.translate("RCC_startup", u"230400", None))
        self.Baud_Rate_comboBox.setItemText(3, QCoreApplication.translate("RCC_startup", u"115200", None))
        self.Baud_Rate_comboBox.setItemText(4, QCoreApplication.translate("RCC_startup", u"57600", None))
        self.Baud_Rate_comboBox.setItemText(5, QCoreApplication.translate("RCC_startup", u"38400", None))
        self.Baud_Rate_comboBox.setItemText(6, QCoreApplication.translate("RCC_startup", u"9600", None))

        self.Baud_Rate_comboBox.setCurrentText(QCoreApplication.translate("RCC_startup", u"115200", None))
        self.Connect_Button.setText(QCoreApplication.translate("RCC_startup", u"Connect!", None))
    # retranslateUi

