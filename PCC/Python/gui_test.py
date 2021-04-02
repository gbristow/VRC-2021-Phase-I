#Qt GUI application for testing the PCC functionality
#written by Patrick Smith
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Qt, QThread, Signal, QObject
from PySide6.QtGui import QColor, QPalette, QFont

from UI_pcc import Ui_VRC_PCC
from startup_widget import Ui_RCC_startup
from serial_utils import serial_ports

from VRC_Peripheral import VRC_peripheral

import sys
import time

class SetupWindow(QWidget):
    def __init__(self, ports):
        super(SetupWindow, self).__init__()
        self.ui = Ui_RCC_startup()
        self.ui.setupUi(self)

        self.ui.COM_Port_comboBox.addItems(ports)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #self.Comms = CommThread()
        self.pcc = None 

        # UNCOMMENT THIS FOR CONNECTING TO SERIAL PORT
        self.setup = SetupWindow(serial_ports())
        self.setup.ui.Connect_Button.clicked.connect(self.connectToPCC)
        self.setup.show()

        self.ui = Ui_VRC_PCC()

    def setupMainWindowUi(self):
        self.ui.setupUi(self)

        # update PWM cmd based on slider / spinbox
        self.ui.pwm_1_cmd.valueChanged.connect(self.updatePWMcmd)
        self.ui.pwm_2_cmd.valueChanged.connect(self.updatePWMcmd)
        self.ui.pwm_3_cmd.valueChanged.connect(self.updatePWMcmd)

        # update RGB LED based on sliders
        self.ui.red_led_slider.valueChanged.connect(self.updateRGBcmd)
        self.ui.green_led_slider.valueChanged.connect(self.updateRGBcmd)
        self.ui.blue_led_slider.valueChanged.connect(self.updateRGBcmd)


    def connectToPCC(self):
        # this function establishes the serial connection to the PCC based on available COM ports
        try:
            port = self.setup.ui.COM_Port_comboBox.currentText()
            baud = self.setup.ui.Baud_Rate_comboBox.currentText()

            self.pcc = VRC_peripheral(port, use_serial=True)

            #TODO - actually write a handshake for the PCC, its all 1 way right now
            #try:
                #self.pcc.handshake(timeout=1)
            #except TimeoutError as e:
                #show error window and close?

            self.setup.close()

            self.setupMainWindowUi()
            self.show()

        except Exception as e:
            print("Error connecting to PCC serial port! ", e)
    

    def updatePWMcmd(self, val):
        # whenever any of the pwm commands change, this function gets called to 
        # update the PCC with the most current PWM commands for all 4 actuators

        # collect the most current pwm commands
        val1 = self.ui.pwm_1_cmd.value()
        val2 = self.ui.pwm_2_cmd.value()
        val3 = self.ui.pwm_3_cmd.value()
        #TODO - add a 4th 
        #val4 = self.ui.pwm_4_cmd.value()

        # send serial message down serial link to PCC
        try:
            self.pcc.set_temp_color([0,val1,val2,val3])
            #TODO - make a raw pwm handler... something like:
            #for i in range(0,4):
                #self.pcc.set_pwm(i,valX)
        except AttributeError as ae:
            print("Can't sent serial command, Serial Port not set up...")

    def updateRGBcmd(self, val):
        # whenever any of the RGB commands change, this function gets called to 
        # update the PCC with the most current RGB commands for the LED strip

        # collect the most current pwm commands
        red = self.ui.red_led_slider.value()
        green = self.ui.green_led_slider.value()
        blue = self.ui.blue_led_slider.value()

        # send serial message down serial link to PCC
        try:
            self.pcc.set_base_color([0,red,green,blue])
        except AttributeError as ae:
            print("Can't sent serial command, Serial Port not set up...")

            
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    app.exec_()

    if window.pcc is not None:
        window.pcc.set_base_color([0,0,0,0])

    sys.exit()

