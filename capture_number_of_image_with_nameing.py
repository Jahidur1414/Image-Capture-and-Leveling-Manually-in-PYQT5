import os
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets                     # uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)              # +++
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from ui import Ui_Form                                   # +++

import test

class video (QtWidgets.QDialog, Ui_Form):
    def __init__(self):
        super().__init__()

#        uic.loadUi('test2.ui',self)                           # ---
        self.setupUi(self)                                     # +++

        self.control_bt.clicked.connect(self.start_webcam)
        #self.capture.clicked.connect(self.capture_image)
        self.capture.hide()

        #-------------------------------------
        #self.bt5.clicked.connect(self.button5)
        self.btn5.hide()

        #self.btn10.clicked.connect(self.button10)
        self.btn10.hide()

        self.btn_exit.clicked.connect(self.exit)

        self.image_label.setScaledContents(True)
        self.cap = None                                        #  -capture <-> +cap

        #self.btnenter.clicked.connect(self.buttonenter)
        self.btnenter.hide()

        self.textbox.hide()

        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 1
        self.name=''
        self.list = {}



    @QtCore.pyqtSlot()
    def start_webcam(self):
        self.control_bt.hide()
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        self.timer.start()
        self.textbox.show()
        self.btnenter.show()
        self.btnenter.clicked.connect(self.buttonenter)

    @QtCore.pyqtSlot()
    def update_frame(self):
        ret, image = self.cap.read()
        simage     = cv2.flip(image, 1)
        self.displayImage(image, True)

    @QtCore.pyqtSlot()
    def capture_image(self):
        print(self.press)
        if self.press > 0:
            print("Done")
            flag, frame = self.cap.read()
            path = r'images/'                         #
            if flag:
                QtWidgets.QApplication.beep()
                name = "{}{}.jpg".format(self.name, self._image_counter)
                cv2.imwrite(os.path.join(path, name), frame)
                self._image_counter += 1
                #print(self.press)
                self.press -=1
        else:
            print("Over Limit")
            self.capture.hide()

    #-------------------------------------
    @QtCore.pyqtSlot()
    def buttonenter(self):
        print("Button Presed !")

        textboxValue = self.textbox.text()

        if not textboxValue:
            print("Empty Value")
            QMessageBox.question(self, 'Message - pythonspot.com', "Please Enter a name" + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.setText("")
            print(textboxValue)
        else:
            QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
            self.textbox.setText("")
            print(textboxValue)
            self.textbox.hide()
            self.btnenter.hide()
            self.name=textboxValue
            #------------------------
            self.btn5.show()
            self.btn5.clicked.connect(self.button5)
            self.btn10.show()
            self.btn10.clicked.connect(self.button10)
            #-------------------------------


    @QtCore.pyqtSlot()
    def button5(self):
        print("Button Presed !")

        self.btn5.hide()
        self.btn10.hide()
        self.press=5
        self.capture.show()
        self.capture.clicked.connect(self.capture_image)

    @QtCore.pyqtSlot()
    def button10(self):
        print("Button Presed")
        self.btn10.hide()
        self.btn5.hide()
        self.press=10
        self.capture.show()
        self.capture.clicked.connect(self.capture_image)


    @QtCore.pyqtSlot()
    def exit(self):
        #exit()
        #exec(open('test.py').read())
        #self.level_image()
        self.close()

    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            self.image_label.setPixmap(QtGui.QPixmap.fromImage(outImage))


class test():
    app = QtWidgets.QApplication(sys.argv)
    window = video()
    window.setWindowTitle('ShopLifting')
    window.show()
    app.exec_()
    print("Testing")
    #exec(open('test.py').read())

if __name__=='__main__':


    sys.exit(test())
