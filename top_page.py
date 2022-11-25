# Form implementation generated from reading ui file 'top_page.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TopWindow(object):
    def setupUi(self, TopWindow):
        TopWindow.setObjectName("TopWindow")
        TopWindow.resize(1920, 1100)
        self.centralwidget = QtWidgets.QWidget(TopWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setEnabled(True)
        self.go_back.setGeometry(QtCore.QRect(870, 990, 200, 60))
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
        self.tableTop = QtWidgets.QTabWidget(self.centralwidget)
        self.tableTop.setGeometry(QtCore.QRect(9, 169, 1491, 811))
        self.tableTop.setMinimumSize(QtCore.QSize(0, 801))
        self.tableTop.setStyleSheet("font: 24pt \"Georgia\";\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.tableTop.setObjectName("tableTop")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableBalances = QtWidgets.QTableWidget(self.tab)
        self.tableBalances.setGeometry(QtCore.QRect(0, 10, 1491, 761))
        self.tableBalances.setObjectName("tableBalances")
        self.tableBalances.setColumnCount(0)
        self.tableBalances.setRowCount(0)
        self.tableTop.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableVikt = QtWidgets.QTableWidget(self.tab_2)
        self.tableVikt.setGeometry(QtCore.QRect(0, 10, 1491, 761))
        self.tableVikt.setObjectName("tableVikt")
        self.tableVikt.setColumnCount(0)
        self.tableVikt.setRowCount(0)
        self.tableTop.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWork = QtWidgets.QTableWidget(self.tab_3)
        self.tableWork.setGeometry(QtCore.QRect(0, 10, 1491, 761))
        self.tableWork.setObjectName("tableWork")
        self.tableWork.setColumnCount(0)
        self.tableWork.setRowCount(0)
        self.tableTop.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableMyTop = QtWidgets.QTableWidget(self.tab_4)
        self.tableMyTop.setGeometry(QtCore.QRect(0, 0, 1491, 771))
        self.tableMyTop.setObjectName("tableMyTop")
        self.tableMyTop.setColumnCount(0)
        self.tableMyTop.setRowCount(0)
        self.tableTop.addTab(self.tab_4, "")
        self.request_txt = QtWidgets.QTextEdit(self.centralwidget)
        self.request_txt.setGeometry(QtCore.QRect(1510, 430, 391, 391))
        self.request_txt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.request_txt.setStyleSheet("font: 18pt \"Courier\";")
        self.request_txt.setObjectName("request_txt")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1510, 180, 391, 251))
        self.label.setStyleSheet("font: 20pt \"Symbol\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(1570, 830, 291, 61))
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.search_btn.setStyleSheet("font: 24pt \"Georgia\";\n"
"background-color: rgb(207, 101, 6);")
        self.search_btn.setObjectName("search_btn")
        TopWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TopWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        TopWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TopWindow)
        self.statusbar.setObjectName("statusbar")
        TopWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TopWindow)
        self.tableTop.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TopWindow)

    def retranslateUi(self, TopWindow):
        _translate = QtCore.QCoreApplication.translate
        TopWindow.setWindowTitle(_translate("TopWindow", "Топы"))
        self.go_back.setText(_translate("TopWindow", "Назад"))
        self.tableTop.setTabText(self.tableTop.indexOf(self.tab), _translate("TopWindow", "По балансам"))
        self.tableTop.setTabText(self.tableTop.indexOf(self.tab_2), _translate("TopWindow", "По отвеченным вопросам в викторине"))
        self.tableTop.setTabText(self.tableTop.indexOf(self.tab_3), _translate("TopWindow", "По решенным загадкам"))
        self.tableTop.setTabText(self.tableTop.indexOf(self.tab_4), _translate("TopWindow", "СВОЙ ТОП"))
        self.request_txt.setHtml(_translate("TopWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">а</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">а</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">аапппву4</p></body></html>"))
        self.label.setText(_translate("TopWindow", "Выберите стандартный топ из\n"
"предложенных либо выберите\n"
"\"Свой топ\" и введите критерий\n"
"для фильтрации! Вводить запрос нужно\n"
"в формате SQL запроса с возможными\n"
"столбцами: username, balance,\n"
"ans_vikt, ans_work. Если\n"
"условий несколько, их нужно\n"
"записать каждый на своей строке"))
        self.search_btn.setText(_translate("TopWindow", "Искать!"))