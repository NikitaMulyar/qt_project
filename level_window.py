# Form implementation generated from reading ui file 'level_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LevelWindow(object):
    def setupUi(self, LevelWindow):
        LevelWindow.setObjectName("LevelWindow")
        LevelWindow.resize(1920, 1100)
        LevelWindow.setBaseSize(QtCore.QSize(1920, 1100))
        self.centralwidget = QtWidgets.QWidget(LevelWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 9, 1881, 1041))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.medium = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.medium.setMinimumSize(QtCore.QSize(400, 100))
        self.medium.setMaximumSize(QtCore.QSize(400, 16777215))
        self.medium.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.medium.setStyleSheet("font: 48pt bold \"Arial\";\n"
"background-color: rgb(254, 204, 102);\n"
"color: rgb(102, 102, 255);")
        self.medium.setObjectName("medium")
        self.gridLayout.addWidget(self.medium, 2, 0, 1, 1)
        self.hard = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.hard.setMinimumSize(QtCore.QSize(400, 100))
        self.hard.setMaximumSize(QtCore.QSize(400, 16777215))
        self.hard.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hard.setStyleSheet("font: 48pt bold \"Arial\";\n"
"background-color: rgb(254, 204, 102);\n"
"color: rgb(128, 0, 2);")
        self.hard.setObjectName("hard")
        self.gridLayout.addWidget(self.hard, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.easy = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.easy.setMinimumSize(QtCore.QSize(400, 100))
        self.easy.setMaximumSize(QtCore.QSize(400, 16777215))
        self.easy.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.easy.setStyleSheet("font: 48pt bold \"Arial\";\n"
"background-color: rgb(254, 204, 102);\n"
"color: rgb(16, 128, 1);")
        self.easy.setObjectName("easy")
        self.gridLayout.addWidget(self.easy, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.go_back = QtWidgets.QPushButton(self.centralwidget)
        self.go_back.setEnabled(True)
        self.go_back.setGeometry(QtCore.QRect(1310, 770, 200, 60))
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
        LevelWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LevelWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 24))
        self.menubar.setObjectName("menubar")
        LevelWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LevelWindow)
        self.statusbar.setObjectName("statusbar")
        LevelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LevelWindow)
        QtCore.QMetaObject.connectSlotsByName(LevelWindow)

    def retranslateUi(self, LevelWindow):
        _translate = QtCore.QCoreApplication.translate
        LevelWindow.setWindowTitle(_translate("LevelWindow", "MainWindow"))
        self.medium.setText(_translate("LevelWindow", "СРЕДНЯЯ"))
        self.hard.setText(_translate("LevelWindow", "СЛОЖНАЯ"))
        self.easy.setText(_translate("LevelWindow", "ЛЕГКАЯ"))
        self.go_back.setText(_translate("LevelWindow", "Назад"))
