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

LOGINED = False
USER_ID = -1
CHECKED = True


class PasswordError(Exception):
    pass


class UsernameError(Exception):
    pass


class LengthError(PasswordError):
    def __str__(self):
        return 'Длина пароля должна быть больше либо равна 8!'


class LetterError(PasswordError):
    def __str__(self):
        return 'В пароле должны быть как заглавные, так и строчные буквы!'


class DigitError(PasswordError):
    def __str__(self):
        return 'В пароле должны присутствовать цифры!'


class SequenceError(PasswordError):
    def __str__(self):
        return 'Нельзя использовать 3 и более подряд идуших символов!'


class WordError(PasswordError):
    def __str__(self):
        return 'В пароле не должно быть слов!'


class NotAlphaAndDigitError(PasswordError):
    def __str__(self):
        return 'Пароль должен состоять только из латинских букв и цифр!'


class UsedError(UsernameError):
    def __str__(self):
        return 'Такой юзернейм уже занят!'


class LenNameError(UsernameError):
    def __str__(self):
        return 'Длина юзернейма должна быть больше либо равна 3!'


dict_words = set()
some_words = set()
f_o = open("top 10000 passwd.txt", encoding="utf-8", mode="r")
f_o2 = open("top-9999-words.txt", encoding="utf-8", mode="r")
for line in f_o:
    line = line.strip('\n')
    some_words.add(line)
for line in f_o2:
    line = line.strip('\n')
    dict_words.add(line)
f_o.close()
f_o2.close()
pc = dict()
mac = dict()
pc1 = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэ', 'ячсмитьбю']
mac1 = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']
cnt = 1
for i in pc1:
    for j in i:
        pc[j] = cnt
        cnt += 1
    cnt = 1
cnt = 1
for i in mac1:
    for j in i:
        mac[j] = cnt
        cnt += 1
    cnt = 1


def check_password(psw):
    if len(psw) < 8:
        raise LengthError
    if psw.lower() == psw or psw.upper() == psw:
        raise LetterError
    for i in psw:
        if i.isdigit():
            break
    else:
        raise DigitError
    for i in range(len(psw) - 4):
        if psw[i].isalpha() and psw[i + 1].isalpha() and psw[i + 2].isalpha():
            if pc[psw[i + 2].lower()] - pc[psw[i + 1].lower()] == \
                    pc[psw[i + 1].lower()] - pc[psw[i].lower()] == 1:
                raise SequenceError
            if mac[psw[i + 2].lower()] - mac[psw[i + 1].lower()] == \
                    mac[psw[i + 1].lower()] - mac[psw[i].lower()] == 1:
                raise SequenceError
    for w in dict_words:
        if w in psw:
            raise WordError
    if not psw.isalnum():
        raise NotAlphaAndDigitError


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


def check_name(name):
    connect = sqlite3.connect('users_db.sqlite3')
    cur = connect.cursor()
    result = cur.execute("""SELECT * FROM users
                WHERE username = ?""", (name,)).fetchall()
    connect.close()
    if len(name) < 3:
        raise LenNameError
    if len(result):
        raise UsedError


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.pushButton.clicked.connect(self.games)

    def games(self):
        stylesheet_choice = """
            ChoiceWindow {
                background-image: url("choice_game.png"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()


class ChoiceWindow(QMainWindow, Ui_ChoiceWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.acc.setIcon(QIcon("acc_icon.png"))
        self.acc.setIconSize(QSize(50, 50))
        self.acc.clicked.connect(self.info)

    def info(self):
        if not LOGINED:
            stylesheet_rol = """
                LogOrRegWindow {
                    background-image: url("acc_new_or_old.png"); 
                    background-repeat: no-repeat; 
                    background-position: center;
                }
            """
            self.rol_w = LogOrRegWindow()
            self.rol_w.setStyleSheet(stylesheet_rol)
            self.rol_w.show()
        else:
            stylesheet_acc = """
                            AccWindow {
                                background-image: url("acc_bg.png"); 
                                background-repeat: no-repeat; 
                                background-position: center;
                            }
                        """
            self.acc_w = AccWindow()
            self.acc_w.setStyleSheet(stylesheet_acc)
            self.acc_w.show()

    def work(self):
        pass


class LogOrRegWindow(QMainWindow, Ui_LogOrRegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.reg_syst_btn.clicked.connect(self.run_r)
        self.log_btn.clicked.connect(self.run_l)

    def run_r(self):
        stylesheet_reg = """
            RegWindow {
                background-image: url("registration.png"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        self.reg_w = RegWindow()
        self.reg_w.setStyleSheet(stylesheet_reg)
        self.reg_w.show()
        self.hide()

    def run_l(self):
        stylesheet_log = """
            LogWindow {
                background-image: url("login_in_system.png"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        self.log_w = LogWindow()
        self.log_w.setStyleSheet(stylesheet_log)
        self.log_w.show()
        self.hide()


class RegWindow(QMainWindow, Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.reg_btn.clicked.connect(self.run)
        self.psw_enter.setEchoMode(QLineEdit.EchoMode.Password)

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
        stylesheet_acc = """
            AccWindow {
                background-image: url("acc_bg.png"); 
                background-repeat: no-repeat; 
                background-position: center;
            }
        """
        self.acc_w = AccWindow()
        self.acc_w.setStyleSheet(stylesheet_acc)
        self.acc_w.show()
        self.hide()


class LogWindow(QMainWindow, Ui_LogWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.log_btn.clicked.connect(self.run)
        self.psw_enter.setEchoMode(QLineEdit.EchoMode.Password)

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
            stylesheet_acc = """
                AccWindow {
                    background-image: url("acc_bg.png"); 
                    background-repeat: no-repeat; 
                    background-position: center;
                }
            """
            self.acc_w = AccWindow()
            self.acc_w.setStyleSheet(stylesheet_acc)
            self.acc_w.show()
            self.hide()
        else:
            error('Неверный юзернейм или пароль!', self)


class AccWindow(QMainWindow, Ui_AccWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.psw_btn.clicked.connect(self.show_hide)
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
        self.filename = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        file = open(self.filename, "rb")
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


stylesheet_main = """
    MainWindow {
        background-image: url("main.png"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

f = 'login_in_system'
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    sys.exit(app.exec())
