# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiedit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui
import time
import keyboard

def clicked():
    time.sleep(5)
    while keyboard.is_pressed("l") == False:
        pyautogui.click()
class Ui_AutoClicker(object):
    def setupUi(self, AutoClicker):
        AutoClicker.setObjectName("AutoClicker")
        AutoClicker.resize(382, 183)
        self.centralwidget = QtWidgets.QWidget(AutoClicker)
        self.centralwidget.setObjectName("centralwidget")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(10, 80, 361, 61))
        self.Start.setObjectName("Start")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 0, 261, 71))
        self.textBrowser.setObjectName("textBrowser")
        AutoClicker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AutoClicker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName("menubar")
        AutoClicker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AutoClicker)
        self.statusbar.setObjectName("statusbar")
        AutoClicker.setStatusBar(self.statusbar)
        self.Start.clicked.connect(clicked)
        self.retranslateUi(AutoClicker)
        QtCore.QMetaObject.connectSlotsByName(AutoClicker)

    def retranslateUi(self, AutoClicker):
        _translate = QtCore.QCoreApplication.translate
        AutoClicker.setWindowTitle(_translate("AutoClicker", "Auto Clicker"))
        self.Start.setText(_translate("AutoClicker", "Start Clicking!"))
        self.textBrowser.setHtml(_translate("AutoClicker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thank you for downloading Auto Clicker! Just simply hit start clicking, and you mouse will start clicking after 5 seconds. To stop clicking, hit the &quot;L&quot; key.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This was created by Hunter Ward as an open source project.</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoClicker = QtWidgets.QMainWindow()
    ui = Ui_AutoClicker()
    ui.setupUi(AutoClicker)
    AutoClicker.show()
    sys.exit(app.exec_())
