# Form implementation generated from reading ui file 'promos.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PromoWindow(object):
    def setupUi(self, PromoWindow):
        PromoWindow.setObjectName("PromoWindow")
        PromoWindow.resize(1920, 1100)
        self.centralwidget = QtWidgets.QWidget(PromoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setEnabled(True)
        self.go_back.setGeometry(QtCore.QRect(690, 970, 200, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_back.sizePolicy().hasHeightForWidth())
        self.go_back.setSizePolicy(sizePolicy)
        self.go_back.setMinimumSize(QtCore.QSize(0, 60))
        self.go_back.setMaximumSize(QtCore.QSize(200, 16777215))
        self.go_back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.go_back.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.go_back.setStyleSheet("QPushButton {\n"
"    font: 75 30pt \"Courier\";\n"
"color: rgb(252, 1, 7);\n"
"background-color: rgb(254, 204, 102);\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(252, 69, 74);\n"
"    font: 32pt \"Courier\";\n"
"}\n"
"")
        self.go_back.setObjectName("go_back")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(500, 230, 921, 621))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.answ_area_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.answ_area_2.setMinimumSize(QtCore.QSize(0, 50))
        self.answ_area_2.setStyleSheet("font: 20pt \"Courier\";")
        self.answ_area_2.setObjectName("answ_area_2")
        self.gridLayout_2.addWidget(self.answ_area_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 20pt \"Tahoma\";\n"
"color: rgb(128, 0, 2);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.check_btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.check_btn_2.setMinimumSize(QtCore.QSize(300, 70))
        self.check_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.check_btn_2.setStyleSheet("\n"
"QPushButton {\n"
"    font: 75 20pt \"Helvetica\";\n"
"background-color: rgb(253, 128, 8);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    font: 75 22pt \"Helvetica\";\n"
"color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.check_btn_2.setObjectName("check_btn_2")
        self.gridLayout_2.addWidget(self.check_btn_2, 0, 2, 1, 1)
        PromoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PromoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        PromoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PromoWindow)
        self.statusbar.setObjectName("statusbar")
        PromoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PromoWindow)
        QtCore.QMetaObject.connectSlotsByName(PromoWindow)

    def retranslateUi(self, PromoWindow):
        _translate = QtCore.QCoreApplication.translate
        PromoWindow.setWindowTitle(_translate("PromoWindow", "Активация промокода"))
        self.go_back.setText(_translate("PromoWindow", "Назад"))
        self.answ_area_2.setText(_translate("PromoWindow", "12345"))
        self.label_3.setText(_translate("PromoWindow", "Введите промокод:"))
        self.check_btn_2.setText(_translate("PromoWindow", "ПРОВЕРИТЬ\n"
"ДЕЙСТВИТЕЛЬНОСТЬ"))
