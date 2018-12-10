# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_win_frm_src.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(273, 110)
        self.centralWidget = QtWidgets.QWidget(window)
        self.centralWidget.setObjectName("centralWidget")
        self.cmdOk = QtWidgets.QPushButton(self.centralWidget)
        self.cmdOk.setGeometry(QtCore.QRect(96, 41, 81, 22))
        self.cmdOk.setObjectName("cmdOk")
        self.txtName = QtWidgets.QLineEdit(self.centralWidget)
        self.txtName.setGeometry(QtCore.QRect(118, 5, 146, 22))
        self.txtName.setObjectName("txtName")
        self.lblName = QtWidgets.QLabel(self.centralWidget)
        self.lblName.setGeometry(QtCore.QRect(6, 8, 107, 16))
        self.lblName.setObjectName("lblName")
        window.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 273, 19))
        self.menuBar.setObjectName("menuBar")
        window.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(window)
        self.mainToolBar.setObjectName("mainToolBar")
        window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "MainWindow"))
        self.cmdOk.setText(_translate("window", "Ok"))
        self.txtName.setText(_translate("window", "Max"))
        self.lblName.setText(_translate("window", "Enter your name: "))

