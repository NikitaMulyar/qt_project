import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLabel, QLineEdit
from PyQt6.QtWidgets import QInputDialog
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize
from main_window import *
from choice_window import *
from acc_info import *
from acc_new_or_old import *
from reg_window import *
from log_window import *
from level_window import *
from work_cmd import *
from vikt import *
from kazino import *
from check_funcs import *
from stylesheets import *
from questions import *
import time


LOGINED = False
USER_ID = -1
MODE = None
HARD_LVL = None


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
            res = cur.execute("""SELECT filename, balance FROM users
                                    WHERE id = ?""", (USER_ID,)).fetchall()[0]
            connect.close()
            if len(res) != 0:
                if res[0] is not None:
                    filename = res[0]
                if res[1] is not None:
                    self.balance_curr_txt.setText(str(res[1]))
        self.acc.setIcon(QIcon(filename))
        self.acc.setIconSize(QSize(50, 50))
        self.acc.clicked.connect(self.info)
        self.go_back.clicked.connect(self.back)
        self.work_btn.clicked.connect(self.choose_lvl)
        self.viktorina_btn.clicked.connect(self.play_vikt)
        self.promo_btn.clicked.connect(self.enter_promo)
        self.top_btn.clicked.connect(self.open_top)
        self.slots_btn.clicked.connect(self.choose_lvl)
        self.kazino_btn.clicked.connect(self.choose_lvl)
        self.shop_btn.clicked.connect(self.open_shop)
        self.crash_btn.clicked.connect(self.choose_lvl)

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

    def choose_lvl(self):
        global MODE
        if USER_ID == -1:
            return
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()
        MODE = self.sender().text()

    def open_shop(self):
        if USER_ID == -1:
            return

    def open_top(self):
        if USER_ID == -1:
            return

    def enter_promo(self):
        if USER_ID == -1:
            return

    def play_vikt(self):
        if USER_ID == -1:
            return
        self.vikt = ViktWindow()
        self.vikt.setStyleSheet(stylesheet_vikt)
        self.vikt.show()
        self.close()


class ViktWindow(QMainWindow, Ui_ViktWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.check_btn.clicked.connect(self.check_ans)
        self.tip_btn.clicked.connect(self.tip_show)
        self.ind = -1
        self.upd()

    def back(self):
        self.ch_w = ChoiceWindow()
        self.ch_w.setStyleSheet(stylesheet_choice)
        self.ch_w.show()
        self.close()

    def check_ans(self):
        msg = QMessageBox(self)
        if self.answ_area.text().lower() == VIKT_A[self.ind].lower():
            add_s = 1200
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f'Верный ответ! Вы заработали: {add_s} монеток!')
            msg.setWindowTitle("Круто!")
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
            curr_blc = cur.execute(f"""SELECT balance FROM users WHERE id = {USER_ID}""").fetchall()[0][0]
            cur.execute(f"""UPDATE users SET balance = {add_s + curr_blc} WHERE id = {USER_ID}""")
            connect.commit()
            connect.close()
            self.upd()
        else:
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText('Неверный ответ!')
            msg.setWindowTitle("Жаль!")
        msg.exec()

    def tip_show(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(VIKT_T.get(self.ind, 'Подсказки на данный вопрос нет.'))
        msg.setWindowTitle("Tip")
        msg.exec()

    def upd(self):
        ind2 = self.ind
        while self.ind == ind2:
            self.ind = random.randint(1, 72)
        self.task_txt.setText(VIKT_Q[self.ind])
        self.answ_area.clear()


class KazWindow(QMainWindow, Ui_KazWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.run_btn.clicked.connect(self.run)
        self.coef_txt.clear()
        self.win_txt.clear()
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        curr_blc = cur.execute(f"""SELECT balance FROM users WHERE id = 
{USER_ID}""").fetchall()[0][0]
        self.curr_txt.setText(str(curr_blc))
        self.stavka_summ.clear()
        self.curr_hard.setText(HARD_LVL)

    def back(self):
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    def run(self):
        try:
            if '-' not in self.stavka_summ.text() and not self.stavka_summ.text().isdigit() or \
                    '-' in self.stavka_summ.text() and self.stavka_summ.text()[1:].isdigit():
                raise NotNumberError
            summ = int(self.stavka_summ.text())
            if summ < 100 or summ > 10000:
                raise NotPositiveNumberError
            if not check_balance(summ, USER_ID):
                raise BigSummError
            ver = random.randint(0, 10000)
            coef = 1
            if HARD_LVL == 'ЛЕГКАЯ':
                if ver < 150:
                    coef = 10
                elif ver < 525:
                    coef = 5
                elif ver < 1500:
                    coef = 2
                elif ver < 3000:
                    coef = 0
                elif ver < 5000:
                    coef = 0.5
                else:
                    coef = 1
            elif HARD_LVL == 'СРЕДНЯЯ':
                if ver < 80:
                    coef = 20
                elif ver < 180:
                    coef = 10
                elif ver < 925:
                    coef = 3
                elif ver < 4000:
                    coef = 1
                elif ver < 5500:
                    coef = 0.75
                elif ver < 8000:
                    coef = 0.5
                else:
                    coef = 0
            elif HARD_LVL == 'СЛОЖНАЯ':
                if ver < 30:
                    coef = 70
                elif ver < 90:
                    coef = 35
                elif ver < 180:
                    coef = 20
                elif ver < 320:
                    coef = 5
                elif ver < 3000:
                    coef = 1
                elif ver < 4500:
                    coef = 0.5
                elif ver < 7000:
                    coef = 0.3
                else:
                    coef = 0
            self.coef_txt.setText(f'x{str(coef)}')
            self.win_txt.setText(str(summ * coef))
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
            curr_blc = cur.execute(f"""SELECT balance FROM users WHERE id = 
            {USER_ID}""").fetchall()[0][0]
            cur.execute(f"""UPDATE users SET balance = {int(curr_blc + summ * coef - summ)} WHERE 
id = {USER_ID}""")
            connect.commit()
            connect.close()
            self.curr_txt.setText(str(int(curr_blc + summ * coef - summ)))
        except Exception as e:
            error(e, self)


class LvlWindow(QMainWindow, Ui_LevelWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.easy.clicked.connect(self.run)
        self.medium.clicked.connect(self.run)
        self.hard.clicked.connect(self.run)

    def back(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()

    def run(self):
        global HARD_LVL, MODE
        HARD_LVL = self.sender().text()
        if MODE == 'Работать':
            self.task_w = ProbSolvWindow()
            self.task_w.setStyleSheet(stylesheet_prob)
            self.task_w.show()
        elif MODE == 'Казино':
            self.kaz_w = KazWindow()
            self.kaz_w.setStyleSheet(stylesheet_kaz)
            self.kaz_w.show()
        self.close()


class ProbSolvWindow(QMainWindow, Ui_ProbSolvWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.check_btn.clicked.connect(self.check_ans)
        self.ind = -1
        self.upd()

    def back(self):
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    def check_ans(self):
        msg = QMessageBox(self)
        if self.answ_area.text() == WORK_Q[HARD_LVL.lower().capitalize()][self.ind][1]:
            add_s = 100
            if HARD_LVL == 'СРЕДНЯЯ':
                add_s = 300
            elif HARD_LVL == 'СЛОЖНАЯ':
                add_s = 600
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f'Верный ответ! Вы заработали: {add_s} монеток!')
            msg.setWindowTitle("Круто!")
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
            curr_blc = cur.execute(f"""SELECT balance FROM users WHERE id = {USER_ID}""").fetchall()[0][0]
            cur.execute(f"""UPDATE users SET balance = {add_s + curr_blc} WHERE id = {USER_ID}""")
            connect.commit()
            connect.close()
            self.upd()
        else:
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText('Неверный ответ!')
            msg.setWindowTitle("Жаль!")
        msg.exec()

    def upd(self):
        ind2 = self.ind
        while self.ind == ind2:
            self.ind = random.randint(0, 14)
        self.task_txt.setText(WORK_Q[HARD_LVL.lower().capitalize()][self.ind][0])
        self.answ_area.clear()


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
        self.name_txt.setText(str(res[0][1]))
        self.psw_txt.setText(str(res[0][2]))
        self.balance_txt.setText(str(res[0][3]))
        self.psw = res[0][2]
        self.psw_btn.setChecked(True)
        self.show_hide()
        self.load_profile_pic.clicked.connect(self.upd_pic)
        self.log_out_btn.clicked.connect(self.log_out_func)
        self.change_name_btn.clicked.connect(self.change_username)
        self.change_psw_btn.clicked.connect(self.change_psw)
        self.del_acc_btn.clicked.connect(self.del_acc)
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
        self.reopen()

    def reopen(self):
        self.acc_w = AccWindow()
        self.acc_w.setStyleSheet(stylesheet_acc)
        self.acc_w.show()
        self.close()

    def open_choice_win(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()

    def log_out_func(self):
        global LOGINED, USER_ID
        LOGINED = False
        USER_ID = -1
        self.ex = MainWindow()
        self.ex.setStyleSheet(stylesheet_main)
        self.ex.show()
        self.close()

    def change_username(self):
        new_name, ok = QInputDialog.getText(self, 'Смена юзернейма',
                                            'Введите новый юзернейм:')
        new_name = str(new_name)
        if ok:
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
            tmp = cur.execute("""SELECT username FROM users WHERE id = ?""",
                              (USER_ID,)).fetchall()[0][0]
            try:
                check_name(new_name, old=tmp)
            except Exception as exp:
                error(exp, self)
                return
            cur.execute("""UPDATE users SET username = ? WHERE id = ?""", (new_name, USER_ID,))
            connect.commit()
            connect.close()
            self.reopen()

    def change_psw(self):
        new_psw, ok = QInputDialog.getText(self, 'Смена пароля',
                                           'Введите новый пароль:',
                                           echo=QLineEdit.EchoMode.Password)
        new_psw = str(new_psw)
        if not ok:
            return
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        tmp = cur.execute("""SELECT password FROM users WHERE id = ?""",
                          (USER_ID,)).fetchall()[0][0]
        try:
            check_password(new_psw, old=tmp)
        except Exception as exp:
            error(exp, self)
        cur.execute("""UPDATE users SET password = ? WHERE id = ?""", (new_psw, USER_ID,))
        connect.commit()
        connect.close()
        self.reopen()

    def del_acc(self):
        global LOGINED, USER_ID
        answer, ok_pressed = QInputDialog.getItem(
            self, "Подтверждение удаления",
            f"Вы действительно хотите удалить аккаунт?",
            ('',), 1, False)
        if not ok_pressed:
            return
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        cur.execute("""DELETE from users WHERE id = ?""", (USER_ID,))
        connect.commit()
        connect.close()
        LOGINED = False
        USER_ID = -1
        self.ex = MainWindow()
        self.ex.setStyleSheet(stylesheet_main)
        self.ex.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    sys.exit(app.exec())
