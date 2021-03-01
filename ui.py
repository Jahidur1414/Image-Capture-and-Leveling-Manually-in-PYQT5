#test2_ui.py
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 386)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)

        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")
        self.verticalLayout.addWidget(self.control_bt)

        self.capture = QtWidgets.QPushButton(Form)
        self.capture.setObjectName("capture")
        self.verticalLayout.addWidget(self.capture)

        #--------------------------------
        self.btn5 = QtWidgets.QPushButton(Form)
        self.btn5.setObjectName("button")
        self.verticalLayout.addWidget(self.btn5)

        self.btn10 = QtWidgets.QPushButton(Form)
        self.btn10.setObjectName("button")
        self.verticalLayout.addWidget(self.btn10)

        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setObjectName("button")
        self.verticalLayout.addWidget(self.btn_exit)

        self.btnenter = QtWidgets.QPushButton(Form)
        self.btnenter.setObjectName("button")
        self.verticalLayout.addWidget(self.btnenter)


        #-------------------------------------------------------
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 20)
        self.textbox.resize(280,40)



        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form",     "Cam view"))
        self.control_bt.setText(_translate("Form", "Start"))
        self.capture.setText(_translate("Form",    "Capture"))
        self.btn5.setText(_translate("Form",    "5"))
        self.btn10.setText(_translate("Form",    "10"))
        self.btn_exit.setText(_translate("Form",    "Exit"))
        self.textbox.setText(_translate("Form",   ""))
        self.btnenter.setText(_translate("Form",    "Enter"))
