# Form implementation generated from reading ui file 'reg_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegWindow(object):
    def setupUi(self, RegWindow):
        RegWindow.setObjectName("RegWindow")
        RegWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(RegWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 230, 1241, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(450, 0))
        self.label.setStyleSheet("font: 30pt bold \"Helvetica\";\n"
"color: rgb(128, 0, 2);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username_enter = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username_enter.setMinimumSize(QtCore.QSize(0, 40))
        self.username_enter.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 20pt \"Courier\";")
        self.username_enter.setText("")
        self.username_enter.setObjectName("username_enter")
        self.gridLayout.addWidget(self.username_enter, 0, 1, 1, 1)
        self.psw_enter = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.psw_enter.setMinimumSize(QtCore.QSize(0, 40))
        self.psw_enter.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 20pt \"Courier\";")
        self.psw_enter.setObjectName("psw_enter")
        self.gridLayout.addWidget(self.psw_enter, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 30pt bold \"Helvetica\";\n"
"color: rgb(128, 0, 2);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.reg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reg_btn.setGeometry(QtCore.QRect(1040, 580, 500, 100))
        self.reg_btn.setMinimumSize(QtCore.QSize(500, 100))
        self.reg_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.reg_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 30pt \"Helvetica\";\n"
"background-color: rgb(226, 118, 43);")
        self.reg_btn.setObjectName("reg_btn")
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setGeometry(QtCore.QRect(1340, 730, 200, 60))
        self.go_back.setMinimumSize(QtCore.QSize(200, 60))
        self.go_back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.go_back.setStyleSheet("font: 75 30pt \"Courier\";\n"
"color: rgb(252, 1, 7);\n"
"background-color: rgb(254, 204, 102);")
        self.go_back.setObjectName("go_back")
        RegWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        RegWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegWindow)
        self.statusbar.setObjectName("statusbar")
        RegWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegWindow)
        QtCore.QMetaObject.connectSlotsByName(RegWindow)

    def retranslateUi(self, RegWindow):
        _translate = QtCore.QCoreApplication.translate
        RegWindow.setWindowTitle(_translate("RegWindow", "Регистрация"))
        self.label.setText(_translate("RegWindow", "Придумайте юзернейм"))
        self.label_3.setText(_translate("RegWindow", "Придумайте пароль"))
        self.reg_btn.setText(_translate("RegWindow", "ЗАРЕГИСТРИРОВАТЬСЯ"))
        self.go_back.setText(_translate("RegWindow", "Назад"))
