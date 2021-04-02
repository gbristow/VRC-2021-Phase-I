# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_pcc.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_VRC_PCC(object):
    def setupUi(self, VRC_PCC):
        if not VRC_PCC.objectName():
            VRC_PCC.setObjectName(u"VRC_PCC")
        VRC_PCC.resize(449, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VRC_PCC.sizePolicy().hasHeightForWidth())
        VRC_PCC.setSizePolicy(sizePolicy)
        VRC_PCC.setMinimumSize(QSize(420, 760))
        font = QFont()
        font.setFamily(u"Arial Black")
        VRC_PCC.setFont(font)
        VRC_PCC.setCursor(QCursor(Qt.ArrowCursor))
        VRC_PCC.setAutoFillBackground(False)
        VRC_PCC.setStyleSheet(u"QMainWindow {\n"
"background: transparent; \n"
"	background-color: rgba(20, 0, 62, 100);\n"
"}\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}\n"
"")
        self.actionManual_Control = QAction(VRC_PCC)
        self.actionManual_Control.setObjectName(u"actionManual_Control")
        self.actionProfile_1 = QAction(VRC_PCC)
        self.actionProfile_1.setObjectName(u"actionProfile_1")
        self.actionProfile_2 = QAction(VRC_PCC)
        self.actionProfile_2.setObjectName(u"actionProfile_2")
        self.actionCOM1 = QAction(VRC_PCC)
        self.actionCOM1.setObjectName(u"actionCOM1")
        self.actionCOM2 = QAction(VRC_PCC)
        self.actionCOM2.setObjectName(u"actionCOM2")
        self.actionCOM3 = QAction(VRC_PCC)
        self.actionCOM3.setObjectName(u"actionCOM3")
        self.actionCOM4 = QAction(VRC_PCC)
        self.actionCOM4.setObjectName(u"actionCOM4")
        self.actionCOM5 = QAction(VRC_PCC)
        self.actionCOM5.setObjectName(u"actionCOM5")
        self.actionCOM6 = QAction(VRC_PCC)
        self.actionCOM6.setObjectName(u"actionCOM6")
        self.actionCOM7 = QAction(VRC_PCC)
        self.actionCOM7.setObjectName(u"actionCOM7")
        self.action57600 = QAction(VRC_PCC)
        self.action57600.setObjectName(u"action57600")
        self.action57600_2 = QAction(VRC_PCC)
        self.action57600_2.setObjectName(u"action57600_2")
        self.action115200 = QAction(VRC_PCC)
        self.action115200.setObjectName(u"action115200")
        self.actionEnter = QAction(VRC_PCC)
        self.actionEnter.setObjectName(u"actionEnter")
        self.actionEnter_2 = QAction(VRC_PCC)
        self.actionEnter_2.setObjectName(u"actionEnter_2")
        self.centralwidget = QWidget(VRC_PCC)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 650))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        self.centralwidget.setFont(font1)
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(400, 730))
        font2 = QFont()
        font2.setFamily(u"Arial Black")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        self.frame_6.setFont(font2)
        self.frame_6.setStyleSheet(u"background-color: rgb(99, 99, 99);\n"
"QLabel {\n"
"	border-radius: 3px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 5px;\n"
"};\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(300, 170))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.frame_10)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 150))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setStyleSheet(u"background-color: rgba(86, 81, 100, 200);\n"
"color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pwm_1_label = QLabel(self.frame_5)
        self.pwm_1_label.setObjectName(u"pwm_1_label")
        self.pwm_1_label.setMinimumSize(QSize(125, 25))
        self.pwm_1_label.setMaximumSize(QSize(125, 20))
        font3 = QFont()
        font3.setFamily(u"Arial Black")
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.pwm_1_label.setFont(font3)
        self.pwm_1_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;")
        self.pwm_1_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.pwm_1_label, 0, Qt.AlignHCenter)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pwm_1_dial = QDial(self.frame_5)
        self.pwm_1_dial.setObjectName(u"pwm_1_dial")
        self.pwm_1_dial.setMinimumSize(QSize(100, 100))
        self.pwm_1_dial.setMaximumSize(QSize(200, 200))
        self.pwm_1_dial.setOrientation(Qt.Horizontal)
        self.pwm_1_dial.setNotchesVisible(True)

        self.horizontalLayout_16.addWidget(self.pwm_1_dial)

        self.pwm_1_cmd = QSpinBox(self.frame_5)
        self.pwm_1_cmd.setObjectName(u"pwm_1_cmd")
        self.pwm_1_cmd.setMaximumSize(QSize(50, 16777215))
        font4 = QFont()
        font4.setFamily(u"Arial Black")
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        self.pwm_1_cmd.setFont(font4)

        self.horizontalLayout_16.addWidget(self.pwm_1_cmd)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.frame_10)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(200, 150))
        self.frame_8.setMaximumSize(QSize(16777215, 250))
        self.frame_8.setStyleSheet(u"background-color: rgba(86, 81, 100, 200);\n"
"color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pwm_2_label = QLabel(self.frame_8)
        self.pwm_2_label.setObjectName(u"pwm_2_label")
        self.pwm_2_label.setMinimumSize(QSize(125, 25))
        self.pwm_2_label.setMaximumSize(QSize(125, 20))
        self.pwm_2_label.setFont(font3)
        self.pwm_2_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;")
        self.pwm_2_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.pwm_2_label, 0, Qt.AlignHCenter)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pwm_2_dial = QDial(self.frame_8)
        self.pwm_2_dial.setObjectName(u"pwm_2_dial")
        self.pwm_2_dial.setMinimumSize(QSize(100, 100))
        self.pwm_2_dial.setMaximumSize(QSize(200, 200))
        self.pwm_2_dial.setOrientation(Qt.Horizontal)
        self.pwm_2_dial.setNotchesVisible(True)

        self.horizontalLayout_17.addWidget(self.pwm_2_dial)

        self.pwm_2_cmd = QSpinBox(self.frame_8)
        self.pwm_2_cmd.setObjectName(u"pwm_2_cmd")
        self.pwm_2_cmd.setMaximumSize(QSize(50, 16777215))
        self.pwm_2_cmd.setFont(font4)

        self.horizontalLayout_17.addWidget(self.pwm_2_cmd)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_10)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 150))
        self.frame_9.setMaximumSize(QSize(16777215, 250))
        self.frame_9.setStyleSheet(u"background-color: rgba(86, 81, 100, 200);\n"
"color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pwm_3_label = QLabel(self.frame_9)
        self.pwm_3_label.setObjectName(u"pwm_3_label")
        self.pwm_3_label.setMinimumSize(QSize(125, 25))
        self.pwm_3_label.setMaximumSize(QSize(125, 20))
        self.pwm_3_label.setFont(font3)
        self.pwm_3_label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;")
        self.pwm_3_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.pwm_3_label, 0, Qt.AlignHCenter)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pwm_3_dial = QDial(self.frame_9)
        self.pwm_3_dial.setObjectName(u"pwm_3_dial")
        self.pwm_3_dial.setMinimumSize(QSize(100, 100))
        self.pwm_3_dial.setMaximumSize(QSize(200, 200))
        self.pwm_3_dial.setOrientation(Qt.Horizontal)
        self.pwm_3_dial.setNotchesVisible(True)

        self.horizontalLayout_18.addWidget(self.pwm_3_dial)

        self.pwm_3_cmd = QSpinBox(self.frame_9)
        self.pwm_3_cmd.setObjectName(u"pwm_3_cmd")
        self.pwm_3_cmd.setMaximumSize(QSize(50, 16777215))
        self.pwm_3_cmd.setFont(font4)

        self.horizontalLayout_18.addWidget(self.pwm_3_cmd)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_10)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(300, 110))
        self.frame_7.setMaximumSize(QSize(5000, 125))
        self.frame_7.setStyleSheet(u"background-color: rgba(86, 81, 100, 200);\n"
"color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_2 = QFrame(self.frame_7)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.GL_direction_label_2 = QLabel(self.frame_2)
        self.GL_direction_label_2.setObjectName(u"GL_direction_label_2")
        self.GL_direction_label_2.setMinimumSize(QSize(100, 25))
        self.GL_direction_label_2.setMaximumSize(QSize(100, 20))
        self.GL_direction_label_2.setFont(font3)
        self.GL_direction_label_2.setStyleSheet(u"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;")
        self.GL_direction_label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.GL_direction_label_2)

        self.red_led_slider = QSlider(self.frame_2)
        self.red_led_slider.setObjectName(u"red_led_slider")
        self.red_led_slider.setMaximum(255)
        self.red_led_slider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.red_led_slider)

        self.GL_direction_label_3 = QLabel(self.frame_2)
        self.GL_direction_label_3.setObjectName(u"GL_direction_label_3")
        self.GL_direction_label_3.setMinimumSize(QSize(100, 25))
        self.GL_direction_label_3.setMaximumSize(QSize(100, 20))
        self.GL_direction_label_3.setFont(font3)
        self.GL_direction_label_3.setStyleSheet(u"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;")
        self.GL_direction_label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.GL_direction_label_3)

        self.green_led_slider = QSlider(self.frame_2)
        self.green_led_slider.setObjectName(u"green_led_slider")
        self.green_led_slider.setMaximum(255)
        self.green_led_slider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.green_led_slider)

        self.GL_direction_label_4 = QLabel(self.frame_2)
        self.GL_direction_label_4.setObjectName(u"GL_direction_label_4")
        self.GL_direction_label_4.setMinimumSize(QSize(100, 25))
        self.GL_direction_label_4.setMaximumSize(QSize(100, 20))
        self.GL_direction_label_4.setFont(font3)
        self.GL_direction_label_4.setStyleSheet(u"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;")
        self.GL_direction_label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.GL_direction_label_4)

        self.blue_led_slider = QSlider(self.frame_2)
        self.blue_led_slider.setObjectName(u"blue_led_slider")
        self.blue_led_slider.setMaximum(255)
        self.blue_led_slider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.blue_led_slider)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rgb_r_cmd = QSpinBox(self.frame)
        self.rgb_r_cmd.setObjectName(u"rgb_r_cmd")
        self.rgb_r_cmd.setMaximumSize(QSize(50, 16777215))
        font5 = QFont()
        font5.setFamily(u"Arial Black")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        self.rgb_r_cmd.setFont(font5)
        self.rgb_r_cmd.setMaximum(255)

        self.verticalLayout_2.addWidget(self.rgb_r_cmd)

        self.rgb_g_cmd = QSpinBox(self.frame)
        self.rgb_g_cmd.setObjectName(u"rgb_g_cmd")
        self.rgb_g_cmd.setMaximumSize(QSize(50, 16777215))
        self.rgb_g_cmd.setFont(font5)
        self.rgb_g_cmd.setMaximum(255)

        self.verticalLayout_2.addWidget(self.rgb_g_cmd)

        self.rgb_b_cmd = QSpinBox(self.frame)
        self.rgb_b_cmd.setObjectName(u"rgb_b_cmd")
        self.rgb_b_cmd.setMaximumSize(QSize(50, 16777215))
        self.rgb_b_cmd.setFont(font5)
        self.rgb_b_cmd.setMaximum(255)

        self.verticalLayout_2.addWidget(self.rgb_b_cmd)


        self.horizontalLayout_8.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_7)


        self.gridLayout.addWidget(self.frame_10, 2, 0, 1, 1)

        self.Title = QLabel(self.frame_6)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(200, 30))
        self.Title.setMaximumSize(QSize(16777215, 25))
        font6 = QFont()
        font6.setFamily(u"Arial Black")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        self.Title.setFont(font6)
        self.Title.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"background-color: rgba(86, 81, 100, 200);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 5px;\n"
"")
        self.Title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.Title, 0, 0, 1, 1)

        self.terminal_console = QTextBrowser(self.frame_6)
        self.terminal_console.setObjectName(u"terminal_console")
        self.terminal_console.setMaximumSize(QSize(16777215, 100))
        font7 = QFont()
        font7.setFamily(u"Monospac821 BT")
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setItalic(False)
        self.terminal_console.setFont(font7)
        self.terminal_console.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
"color: rgb(0, 200, 0);\n"
"")

        self.gridLayout.addWidget(self.terminal_console, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_6)

        VRC_PCC.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(VRC_PCC)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy1)
        self.statusbar.setStyleSheet(u"")
        VRC_PCC.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(VRC_PCC)
        self.pwm_1_dial.valueChanged.connect(self.pwm_1_cmd.setValue)
        self.pwm_1_cmd.valueChanged.connect(self.pwm_1_dial.setValue)
        self.pwm_2_dial.valueChanged.connect(self.pwm_2_cmd.setValue)
        self.pwm_2_cmd.valueChanged.connect(self.pwm_2_dial.setValue)
        self.pwm_3_dial.valueChanged.connect(self.pwm_3_cmd.setValue)
        self.pwm_3_cmd.valueChanged.connect(self.pwm_3_dial.setValue)
        self.red_led_slider.valueChanged.connect(self.rgb_r_cmd.setValue)
        self.rgb_r_cmd.valueChanged.connect(self.red_led_slider.setValue)
        self.green_led_slider.valueChanged.connect(self.rgb_g_cmd.setValue)
        self.rgb_g_cmd.valueChanged.connect(self.green_led_slider.setValue)
        self.blue_led_slider.valueChanged.connect(self.rgb_b_cmd.setValue)
        self.rgb_b_cmd.valueChanged.connect(self.blue_led_slider.setValue)

        QMetaObject.connectSlotsByName(VRC_PCC)
    # setupUi

    def retranslateUi(self, VRC_PCC):
        VRC_PCC.setWindowTitle(QCoreApplication.translate("VRC_PCC", u"VRC Peripheral Control Computer", None))
        self.actionManual_Control.setText(QCoreApplication.translate("VRC_PCC", u"Manual Control", None))
        self.actionProfile_1.setText(QCoreApplication.translate("VRC_PCC", u"Profile 1", None))
        self.actionProfile_2.setText(QCoreApplication.translate("VRC_PCC", u"Profile 2", None))
        self.actionCOM1.setText(QCoreApplication.translate("VRC_PCC", u"COM1", None))
        self.actionCOM2.setText(QCoreApplication.translate("VRC_PCC", u"COM2", None))
        self.actionCOM3.setText(QCoreApplication.translate("VRC_PCC", u"COM3", None))
        self.actionCOM4.setText(QCoreApplication.translate("VRC_PCC", u"COM4", None))
        self.actionCOM5.setText(QCoreApplication.translate("VRC_PCC", u"COM5", None))
        self.actionCOM6.setText(QCoreApplication.translate("VRC_PCC", u"COM6", None))
        self.actionCOM7.setText(QCoreApplication.translate("VRC_PCC", u"COM7", None))
        self.action57600.setText(QCoreApplication.translate("VRC_PCC", u"9600", None))
        self.action57600_2.setText(QCoreApplication.translate("VRC_PCC", u"57600", None))
        self.action115200.setText(QCoreApplication.translate("VRC_PCC", u"115200", None))
        self.actionEnter.setText(QCoreApplication.translate("VRC_PCC", u"Enter...", None))
        self.actionEnter_2.setText(QCoreApplication.translate("VRC_PCC", u"Enter...", None))
        self.pwm_1_label.setText(QCoreApplication.translate("VRC_PCC", u"PWM 1 Command", None))
        self.pwm_2_label.setText(QCoreApplication.translate("VRC_PCC", u"PWM 2 Command", None))
        self.pwm_3_label.setText(QCoreApplication.translate("VRC_PCC", u"PWM 3 Command", None))
        self.GL_direction_label_2.setText(QCoreApplication.translate("VRC_PCC", u"Red", None))
        self.GL_direction_label_3.setText(QCoreApplication.translate("VRC_PCC", u"Green", None))
        self.GL_direction_label_4.setText(QCoreApplication.translate("VRC_PCC", u"Blue", None))
        self.Title.setText(QCoreApplication.translate("VRC_PCC", u"VRC Peripheral Control Computer", None))
    # retranslateUi

