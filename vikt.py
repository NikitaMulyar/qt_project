# Form implementation generated from reading ui file 'vikt.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ViktWindow(object):
    def setupUi(self, ViktWindow):
        ViktWindow.setObjectName("ViktWindow")
        ViktWindow.resize(1920, 1100)
        self.centralwidget = QtWidgets.QWidget(ViktWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 280, 1671, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tip_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tip_btn.setMinimumSize(QtCore.QSize(300, 70))
        self.tip_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tip_btn.setStyleSheet("font: 75 24pt \"Helvetica\";\n"
"background-color: rgb(253, 128, 8);\n"
"color: rgb(255, 255, 255);")
        self.tip_btn.setObjectName("tip_btn")
        self.gridLayout.addWidget(self.tip_btn, 1, 4, 1, 1)
        self.check_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.check_btn.setMinimumSize(QtCore.QSize(300, 70))
        self.check_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.check_btn.setStyleSheet("font: 75 24pt \"Helvetica\";\n"
"background-color: rgb(253, 128, 8);\n"
"color: rgb(255, 255, 255);")
        self.check_btn.setObjectName("check_btn")
        self.gridLayout.addWidget(self.check_btn, 1, 2, 1, 1)
        self.answ_area = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.answ_area.setMinimumSize(QtCore.QSize(0, 50))
        self.answ_area.setStyleSheet("font: italic 24pt \"Times New Roman\";")
        self.answ_area.setObjectName("answ_area")
        self.gridLayout.addWidget(self.answ_area, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 24pt \"Symbol\";\n"
"color: rgb(128, 0, 2);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.task_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.task_txt.setStyleSheet("font: 24pt \"Symbol\";\n"
"color: rgb(0, 0, 0);")
        self.task_txt.setObjectName("task_txt")
        self.gridLayout.addWidget(self.task_txt, 0, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setEnabled(True)
        self.go_back.setGeometry(QtCore.QRect(261, 941, 200, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_back.sizePolicy().hasHeightForWidth())
        self.go_back.setSizePolicy(sizePolicy)
        self.go_back.setMinimumSize(QtCore.QSize(0, 60))
        self.go_back.setMaximumSize(QtCore.QSize(200, 16777215))
        self.go_back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.go_back.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.go_back.setStyleSheet("font: 75 36pt \"Courier\";\n"
"color: rgb(252, 1, 7);\n"
"background-color: rgb(254, 204, 102);\n"
"")
        self.go_back.setObjectName("go_back")
        ViktWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ViktWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        ViktWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ViktWindow)
        self.statusbar.setObjectName("statusbar")
        ViktWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ViktWindow)
        QtCore.QMetaObject.connectSlotsByName(ViktWindow)

    def retranslateUi(self, ViktWindow):
        _translate = QtCore.QCoreApplication.translate
        ViktWindow.setWindowTitle(_translate("ViktWindow", "Викторина"))
        self.tip_btn.setText(_translate("ViktWindow", "ПОДСКАЗКА"))
        self.check_btn.setText(_translate("ViktWindow", "ПРОВЕРИТЬ!"))
        self.answ_area.setText(_translate("ViktWindow", "12345"))
        self.label_2.setText(_translate("ViktWindow", "Ответ:"))
        self.task_txt.setText(_translate("ViktWindow", "Задание. "))
        self.go_back.setText(_translate("ViktWindow", "Назад"))
