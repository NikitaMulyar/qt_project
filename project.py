import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLabel, QLineEdit
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize
from PIL.ImageQt import ImageQt
from PIL import Image
from main_window import *
from choice_window import *
from acc_info import *
from acc_new_or_old import *
from reg_window import *
from log_window import *
from exceptions import *
from check_funcs import *
from stylesheets import *

LOGINED = False
USER_ID = -1
CHECKED = True


def error(exp, self):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText(str(exp))
    msg.setWindowTitle("Ошибка")
    msg.exec()


def append_user(name, psw):
    connect = sqlite3.connect('users_db.sqlite3')
    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO users(username, password, balance) VALUES('{name}', '{psw}', 0)")
    connect.commit()
    connect.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.pushButton.clicked.connect(self.games)

    def games(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()


class ChoiceWindow(QMainWindow, Ui_ChoiceWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        filename = 'acc_icon.png'
        if USER_ID != -1:
            res = cur.execute("""SELECT filename FROM users
                                    WHERE id = ?""", (USER_ID,)).fetchall()
            connect.close()
            if len(res) != 0:
                filename = res[0][0]
        self.acc.setIcon(QIcon(filename))
        self.acc.setIconSize(QSize(50, 50))
        self.acc.clicked.connect(self.info)
        self.go_back.clicked.connect(self.back)

    def info(self):
        if not LOGINED:
            self.rol_w = LogOrRegWindow()
            self.rol_w.setStyleSheet(stylesheet_rol)
            self.rol_w.show()
            self.close()
        else:
            self.acc_w = AccWindow()
            self.acc_w.setStyleSheet(stylesheet_acc)
            self.acc_w.show()
            self.close()

    def back(self):
        self.main_w = MainWindow()
        self.main_w.setStyleSheet(stylesheet_main)
        self.main_w.show()
        self.close()

    def work(self):
        pass


class LogOrRegWindow(QMainWindow, Ui_LogOrRegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.reg_syst_btn.clicked.connect(self.run_r)
        self.log_btn.clicked.connect(self.run_l)
        self.go_back.clicked.connect(self.back)

    def run_r(self):
        self.reg_w = RegWindow()
        self.reg_w.setStyleSheet(stylesheet_reg)
        self.reg_w.show()
        self.hide()

    def run_l(self):
        self.log_w = LogWindow()
        self.log_w.setStyleSheet(stylesheet_log)
        self.log_w.show()
        self.hide()

    def back(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()


class RegWindow(QMainWindow, Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.reg_btn.clicked.connect(self.run)
        self.psw_enter.setEchoMode(QLineEdit.EchoMode.Password)
        self.go_back.clicked.connect(self.back)

    def run(self):
        global LOGINED, USER_ID
        name = self.username_enter.text()
        psw = self.psw_enter.text()
        try:
            check_name(name)
            check_password(psw)
        except Exception as exp:
            error(exp, self)
            return
        LOGINED = True
        append_user(name, psw)
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        USER_ID = int(cur.execute("""SELECT id FROM users
                        WHERE username = ? and password = ?""", (name, psw,)).fetchall()[0][0])
        connect.close()
        self.acc_w = AccWindow()
        self.acc_w.setStyleSheet(stylesheet_acc)
        self.acc_w.show()
        self.hide()

    def back(self):
        self.rol_w = LogOrRegWindow()
        self.rol_w.setStyleSheet(stylesheet_rol)
        self.rol_w.show()
        self.close()


class LogWindow(QMainWindow, Ui_LogWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.log_btn.clicked.connect(self.run)
        self.psw_enter.setEchoMode(QLineEdit.EchoMode.Password)
        self.go_back.clicked.connect(self.back)

    def run(self):
        global LOGINED, USER_ID
        name = self.username_enter.text()
        psw = self.psw_enter.text()
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        result = cur.execute("""SELECT * FROM users
                        WHERE username = ? and password = ?""", (name, psw,)).fetchall()
        connect.close()
        if len(result):
            LOGINED = True
            USER_ID = int(result[0][0])
            self.acc_w = AccWindow()
            self.acc_w.setStyleSheet(stylesheet_acc)
            self.acc_w.show()
            self.close()
        else:
            error('Неверный юзернейм или пароль!', self)

    def back(self):
        self.rol_w = LogOrRegWindow()
        self.rol_w.setStyleSheet(stylesheet_rol)
        self.rol_w.show()
        self.close()


class AccWindow(QMainWindow, Ui_AccWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.psw_btn.clicked.connect(self.show_hide)
        self.go_back.clicked.connect(self.open_choice_win)
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        res = cur.execute("""SELECT * FROM users
                        WHERE id = ?""", (USER_ID,)).fetchall()
        connect.close()
        self.id_txt.setText(str(USER_ID))
        self.name_txt.setText(res[0][1])
        self.psw_txt.setText(res[0][2])
        self.balance_txt.setText(str(res[0][3]))
        self.psw = res[0][2]
        self.psw_btn.setChecked(CHECKED)
        self.show_hide()
        self.load_profile_pic.clicked.connect(self.upd_pic)
        pic = res[0][4]
        self.pixmap = QPixmap()
        if pic is not None:
            self.pixmap.loadFromData(pic, res[0][5].split('.')[-1])
            self.image = QLabel(self)
            self.image.setPixmap(self.pixmap)
            self.image.setScaledContents(True)
            self.image.move(420, 180)
            self.image.resize(100, 100)

    def show_hide(self):
        status = self.psw_btn.isChecked()
        if status:
            self.psw_txt.setText('*****')
        else:
            self.psw_txt.setText(self.psw)

    def upd_pic(self):
        try:
            self.filename = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
            file = open(self.filename, "rb")
        except Exception:
            return
        data = sqlite3.Binary(file.read())
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        cur.execute("""UPDATE users SET profile_pic = ?, filename = ?
                                WHERE id = ?""", (data, self.filename,
                                                  USER_ID,))
        connect.commit()
        connect.close()
        self.pixmap.loadFromData(data, self.filename.split('.')[-1])
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)
        self.image.move(420, 180)
        self.image.resize(100, 100)
        self.acc_w = AccWindow()
        self.acc_w.setStyleSheet(stylesheet_acc)
        self.acc_w.show()
        self.close()

    def open_choice_win(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    sys.exit(app.exec())
