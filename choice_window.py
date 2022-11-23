# Form implementation generated from reading ui file 'choice_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChoiceWindow(object):
    def setupUi(self, ChoiceWindow):
        ChoiceWindow.setObjectName("ChoiceWindow")
        ChoiceWindow.setEnabled(True)
        ChoiceWindow.resize(1920, 1080)
        ChoiceWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        ChoiceWindow.setBaseSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(ChoiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 150, 1801, 611))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.top_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.top_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.top_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.top_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.top_btn.setObjectName("top_btn")
        self.gridLayout.addWidget(self.top_btn, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(200, 50))
        self.label_7.setStyleSheet("color: rgb(205, 0, 18);\n"
"font: 36pt \"Arial Black\";\n"
"background-color: rgba(254, 184, 43, 128);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)
        self.shop_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.shop_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.shop_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.shop_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.shop_btn.setObjectName("shop_btn")
        self.gridLayout.addWidget(self.shop_btn, 3, 3, 1, 1)
        self.crash_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.crash_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.crash_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.crash_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.crash_btn.setObjectName("crash_btn")
        self.gridLayout.addWidget(self.crash_btn, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("color: rgb(205, 0, 18);\n"
"font: 36pt \"Arial Black\";\n"
"background-color: rgba(254, 184, 43, 128);")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(200, 50))
        self.label_6.setStyleSheet("color: rgb(205, 0, 18);\n"
"font: 36pt \"Arial Black\";\n"
"background-color: rgba(254, 184, 43, 128);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("color: rgb(205, 0, 18);\n"
"font: 36pt \"Arial Black\";\n"
"background-color: rgba(254, 184, 43, 128);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.kazino_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.kazino_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.kazino_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.kazino_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.kazino_btn.setObjectName("kazino_btn")
        self.gridLayout.addWidget(self.kazino_btn, 2, 0, 1, 1)
        self.viktorina_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.viktorina_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.viktorina_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.viktorina_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.viktorina_btn.setObjectName("viktorina_btn")
        self.gridLayout.addWidget(self.viktorina_btn, 2, 3, 1, 1)
        self.work_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.work_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.work_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.work_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.work_btn.setObjectName("work_btn")
        self.gridLayout.addWidget(self.work_btn, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 4, 1, 1)
        self.slots_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.slots_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.slots_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.slots_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.slots_btn.setObjectName("slots_btn")
        self.gridLayout.addWidget(self.slots_btn, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 1, 1, 1)
        self.promo_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.promo_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.promo_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.promo_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(253, 102, 102);")
        self.promo_btn.setObjectName("promo_btn")
        self.gridLayout.addWidget(self.promo_btn, 4, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setStyleSheet("background-color: rgba(0, 0, 0, 128);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Verdana\";")
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 4, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(59, 759, 551, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("font: 24pt \"Arial\";\n"
"color: rgb(128, 0, 2);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.balance_curr_txt = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.balance_curr_txt.setMinimumSize(QtCore.QSize(400, 0))
        self.balance_curr_txt.setStyleSheet("color: rgb(252, 1, 7);\n"
"font: 75 36pt \"Courier\";")
        self.balance_curr_txt.setObjectName("balance_curr_txt")
        self.horizontalLayout.addWidget(self.balance_curr_txt)
        self.acc = QtWidgets.QPushButton(self.centralwidget)
        self.acc.setGeometry(QtCore.QRect(1650, 30, 250, 50))
        self.acc.setMinimumSize(QtCore.QSize(250, 50))
        self.acc.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.acc.setStyleSheet("background-color: rgba(255, 255, 255, 40);\n"
"font: 30pt \"Arial\";\n"
"color: rgb(128, 0, 2);")
        self.acc.setObjectName("acc")
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setGeometry(QtCore.QRect(1160, 940, 191, 71))
        self.go_back.setMinimumSize(QtCore.QSize(0, 60))
        self.go_back.setMaximumSize(QtCore.QSize(200, 16777215))
        self.go_back.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.go_back.setStyleSheet("font: 75 36pt \"Courier\";\n"
"color: rgb(252, 1, 7);\n"
"background-color: rgb(254, 204, 102);")
        self.go_back.setObjectName("go_back")
        ChoiceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChoiceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        ChoiceWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChoiceWindow)
        self.statusbar.setObjectName("statusbar")
        ChoiceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoiceWindow)

    def retranslateUi(self, ChoiceWindow):
        _translate = QtCore.QCoreApplication.translate
        ChoiceWindow.setWindowTitle(_translate("ChoiceWindow", "Команды"))
        self.top_btn.setText(_translate("ChoiceWindow", "Топ"))
        self.label_7.setText(_translate("ChoiceWindow", "Команда"))
        self.shop_btn.setText(_translate("ChoiceWindow", "Магазин"))
        self.crash_btn.setText(_translate("ChoiceWindow", "Краш-казино"))
        self.label_8.setText(_translate("ChoiceWindow", "Описание\n"
"команды"))
        self.label_6.setText(_translate("ChoiceWindow", "Команда"))
        self.label_5.setText(_translate("ChoiceWindow", "Описание\n"
"команды"))
        self.kazino_btn.setText(_translate("ChoiceWindow", "Казино"))
        self.viktorina_btn.setText(_translate("ChoiceWindow", "Викторина"))
        self.work_btn.setText(_translate("ChoiceWindow", "Работать"))
        self.label_2.setText(_translate("ChoiceWindow", "Решите загадку и\n"
"получите фиксированное\n"
"вознаграждение!"))
        self.label_11.setText(_translate("ChoiceWindow", "Сделайте ставку и\n"
"попытайте свою удачу -\n"
"главный приз - множитель\n"
"x200!"))
        self.label_14.setText(_translate("ChoiceWindow", "Узнайте, кто сейчас на первом месте!"))
        self.label_13.setText(_translate("ChoiceWindow", "Сделайте ставку и коэффициент - если\n"
"выпавший коэффициент больше либо\n"
"равен вашему, то вы получите\n"
"ваш приз в рамезере вашей ставки\n"
"на ваш поставленный коэффициент"))
        self.label_12.setText(_translate("ChoiceWindow", "Ответьте на вопрос и\n"
"получите денежный приз!"))
        self.label_15.setText(_translate("ChoiceWindow", "Обменяйте ваши деньги на призы!"))
        self.slots_btn.setText(_translate("ChoiceWindow", "Слоты"))
        self.label_16.setText(_translate("ChoiceWindow", "Весь выигрыш зависит от\n"
"выпавших фруктов!"))
        self.promo_btn.setText(_translate("ChoiceWindow", "Ввести промокод"))
        self.label_17.setText(_translate("ChoiceWindow", "Иногда публикуются промокоды...\n"
"Вы их можете ввести и получить приз!"))
        self.label.setText(_translate("ChoiceWindow", "Ваш баланс:"))
        self.balance_curr_txt.setText(_translate("ChoiceWindow", "0"))
        self.acc.setText(_translate("ChoiceWindow", "Мой Аккаунт"))
        self.go_back.setText(_translate("ChoiceWindow", "Назад"))
