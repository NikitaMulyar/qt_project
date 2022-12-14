# Form implementation generated from reading ui file 'acc_info.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AccWindow(object):
    def setupUi(self, AccWindow):
        AccWindow.setObjectName("AccWindow")
        AccWindow.resize(1920, 1080)
        AccWindow.setBaseSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(AccWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(239, 139, 1451, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 90))
        self.label_5.setStyleSheet("font: 25 italic 20pt \"Helvetica\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.place_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.place_txt.setStyleSheet("color: rgb(128, 0, 2);\n"
"font: 20pt \"Courier\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"")
        self.place_txt.setObjectName("place_txt")
        self.gridLayout.addWidget(self.place_txt, 4, 3, 1, 2)
        self.id_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.id_txt.setStyleSheet("color: rgb(128, 0, 2);\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"font: 20pt \"Courier\";\n"
"")
        self.id_txt.setObjectName("id_txt")
        self.gridLayout.addWidget(self.id_txt, 0, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.balance_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.balance_txt.setStyleSheet("color: rgb(128, 0, 2);\n"
"font: 20pt \"Courier\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"")
        self.balance_txt.setObjectName("balance_txt")
        self.gridLayout.addWidget(self.balance_txt, 3, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(3)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 25 italic 20pt \"Helvetica\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 90))
        self.label_4.setStyleSheet("font: 25 italic 20pt \"Helvetica\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.name_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name_txt.setStyleSheet("color: rgb(128, 0, 2);\n"
"font: 20pt \"Courier\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"")
        self.name_txt.setObjectName("name_txt")
        self.gridLayout.addWidget(self.name_txt, 1, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 90))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.label_3.setStyleSheet("font: 25 italic 20pt \"Helvetica\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 90))
        self.label_6.setStyleSheet("font: 25 italic 20pt \"Helvetica\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-left-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 5, 1, 1)
        self.psw_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.psw_btn.setMaximumSize(QtCore.QSize(250, 16777215))
        self.psw_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.psw_btn.setStyleSheet("font: 25 italic 20pt \"Helvetica\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-right-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.psw_btn.setIconSize(QtCore.QSize(50, 50))
        self.psw_btn.setObjectName("psw_btn")
        self.gridLayout.addWidget(self.psw_btn, 2, 5, 1, 1)
        self.psw_txt = QtWidgets.QLabel(self.gridLayoutWidget)
        self.psw_txt.setMinimumSize(QtCore.QSize(350, 0))
        self.psw_txt.setStyleSheet("color: rgb(128, 0, 2);\n"
"font: 20pt \"Courier\";\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-top-color: rgb(0, 0, 0);\n"
"")
        self.psw_txt.setObjectName("psw_txt")
        self.gridLayout.addWidget(self.psw_txt, 2, 3, 1, 2)
        self.open_invent = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_invent.setMinimumSize(QtCore.QSize(0, 90))
        self.open_invent.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.open_invent.setStyleSheet("QPushButton {\n"
"    background-color: rgba(47, 106, 255, 194);\n"
"font: 20pt \"Courier\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"font: 22pt \"Courier\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.open_invent.setObjectName("open_invent")
        self.gridLayout.addWidget(self.open_invent, 4, 6, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 650, 1570, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_11.setStyleSheet("font: 75 30pt \"Helvetica\";\n"
"color: rgb(252, 1, 7);\n"
"background-color: rgba(253, 128, 8, 128);")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_psw_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.change_psw_btn.setMinimumSize(QtCore.QSize(300, 60))
        self.change_psw_btn.setMaximumSize(QtCore.QSize(300, 60))
        self.change_psw_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.change_psw_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(15, 128, 255);\n"
"background-color: rgba(255, 255, 255, 64);\n"
"font: 20pt \"Courier\";\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(23, 43, 255);\n"
"font: 22pt \"Courier\";\n"
"}\n"
"")
        self.change_psw_btn.setObjectName("change_psw_btn")
        self.horizontalLayout.addWidget(self.change_psw_btn)
        self.change_name_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.change_name_btn.setMinimumSize(QtCore.QSize(300, 60))
        self.change_name_btn.setMaximumSize(QtCore.QSize(300, 60))
        self.change_name_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.change_name_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(15, 128, 255);\n"
"background-color: rgba(255, 255, 255, 64);\n"
"font: 20pt \"Courier\";\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(23, 43, 255);\n"
"font: 22pt \"Courier\";\n"
"}\n"
"")
        self.change_name_btn.setObjectName("change_name_btn")
        self.horizontalLayout.addWidget(self.change_name_btn)
        self.log_out_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.log_out_btn.setMinimumSize(QtCore.QSize(300, 60))
        self.log_out_btn.setMaximumSize(QtCore.QSize(300, 60))
        self.log_out_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.log_out_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(15, 128, 255);\n"
"background-color: rgba(255, 255, 255, 64);\n"
"font: 20pt \"Courier\";\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(23, 43, 255);\n"
"font: 22pt \"Courier\";\n"
"}\n"
"")
        self.log_out_btn.setObjectName("log_out_btn")
        self.horizontalLayout.addWidget(self.log_out_btn)
        self.load_profile_pic = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_profile_pic.setMinimumSize(QtCore.QSize(300, 60))
        self.load_profile_pic.setMaximumSize(QtCore.QSize(300, 60))
        self.load_profile_pic.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.load_profile_pic.setStyleSheet("QPushButton {\n"
"    color: rgb(15, 128, 255);\n"
"background-color: rgba(255, 255, 255, 64);\n"
"font: 20pt \"Courier\";\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(23, 43, 255);\n"
"font: 22pt \"Courier\";\n"
"}\n"
"")
        self.load_profile_pic.setObjectName("load_profile_pic")
        self.horizontalLayout.addWidget(self.load_profile_pic)
        self.del_acc_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.del_acc_btn.setMinimumSize(QtCore.QSize(300, 60))
        self.del_acc_btn.setMaximumSize(QtCore.QSize(300, 60))
        self.del_acc_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.del_acc_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(15, 128, 255);\n"
"background-color: rgba(255, 255, 255, 64);\n"
"font: 20pt \"Courier\";\n"
"border-radius: 15px;\n"
"border: 2px solid rgb(228, 13, 5);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(23, 43, 255);\n"
"font: 22pt \"Courier\";\n"
"}\n"
"")
        self.del_acc_btn.setObjectName("del_acc_btn")
        self.horizontalLayout.addWidget(self.del_acc_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setGeometry(QtCore.QRect(1100, 890, 200, 60))
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
        AccWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AccWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        AccWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AccWindow)
        self.statusbar.setObjectName("statusbar")
        AccWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AccWindow)
        QtCore.QMetaObject.connectSlotsByName(AccWindow)

    def retranslateUi(self, AccWindow):
        _translate = QtCore.QCoreApplication.translate
        AccWindow.setWindowTitle(_translate("AccWindow", "Информация"))
        self.label_5.setText(_translate("AccWindow", "Место в топе"))
        self.place_txt.setText(_translate("AccWindow", "0"))
        self.id_txt.setText(_translate("AccWindow", "0"))
        self.balance_txt.setText(_translate("AccWindow", "0"))
        self.label_2.setText(_translate("AccWindow", "Ваш ID"))
        self.label_4.setText(_translate("AccWindow", "Юзернейм"))
        self.name_txt.setText(_translate("AccWindow", "0"))
        self.label_3.setText(_translate("AccWindow", "Пароль"))
        self.label_6.setText(_translate("AccWindow", "Баланс"))
        self.psw_btn.setText(_translate("AccWindow", "Показать/\n"
"Скрыть"))
        self.psw_txt.setText(_translate("AccWindow", "***"))
        self.open_invent.setText(_translate("AccWindow", "Инвентарь"))
        self.label_11.setText(_translate("AccWindow", "Действия"))
        self.change_psw_btn.setText(_translate("AccWindow", "Сменить пароль"))
        self.change_name_btn.setText(_translate("AccWindow", "Сменить юзернейм"))
        self.log_out_btn.setText(_translate("AccWindow", "Выйти из профиля"))
        self.load_profile_pic.setText(_translate("AccWindow", "Новая аватарка"))
        self.del_acc_btn.setText(_translate("AccWindow", "Удалить аккаунт"))
        self.go_back.setText(_translate("AccWindow", "Назад"))
