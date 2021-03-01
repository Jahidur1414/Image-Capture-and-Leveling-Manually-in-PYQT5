import os
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets                     # uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout)              # +++

from test2_ui import Ui_Form                                   # +++

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

        self.timer = QtCore.QTimer(self, interval=5)
        self.timer.timeout.connect(self.update_frame)
        self._image_counter = 1
        self.press=0

    @QtCore.pyqtSlot()
    def start_webcam(self):
        self.control_bt.hide()
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
        self.timer.start()
        self.btn5.show()
        self.btn5.clicked.connect(self.button5)
        self.btn10.show()
        self.btn10.clicked.connect(self.button10)

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
                name = "my_image {}.jpg".format(self._image_counter)
                cv2.imwrite(os.path.join(path, name), frame)
                self._image_counter += 1
                #print(self.press)
                self.press -=1
        else:
            print("Over Limit")
            self.capture.hide()

    #-------------------------------------
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
        exit()

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

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = video()
    window.setWindowTitle('ShopLifting')
    window.show()
    sys.exit(app.exec_())
