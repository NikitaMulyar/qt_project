import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLabel, QLineEdit
from PyQt6.QtWidgets import QInputDialog, QTableWidgetItem, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QColor
from PyQt6.QtCore import QSize, QTimer
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
from sloty import *
from promocodes import *
from promos import *
from crash import *
from top_page import *


LOGINED = False
ACC_OBJ = None
USER_ID = -1
MODE = None
HARD_LVL = None
EMOJIS = ['\U0001F95D', '\U0001F34E', '\U0001F351', '\U0001F34F', '\U0001F350', '\U0001F353',
          '\U0001F34C', '\U0001F34A', '\U0001F34B', '\U0001F349', '\U0001F347', '\U0001F352',
          '\U0001F34D', '\U0001F348']


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


def set_table(array, table):
    for i, row in enumerate(array):
        table.setRowCount(table.rowCount() + 1)
        for j, elem in enumerate(row):
            if j == 0 and elem[0] is None:
                table.setItem(i, j, QTableWidgetItem('Нет аватарки'))
                continue
            elif j == 0 and elem[0] is not None:
                pixmap = QPixmap()
                pixmap.loadFromData(elem[0], elem[1])
                icon = QIcon()
                icon.addPixmap(pixmap)
                item = QTableWidgetItem(icon, '')
                table.setItem(i, j, item)
                table.horizontalHeader().resizeSection(j, 210)
            else:
                table.setItem(i, j, QTableWidgetItem(str(elem)))
                table.horizontalHeader().resizeSection(j, 250)
            if i == 0:
                table.item(i, j).setBackground(QColor(255, 215, 0))
            elif i == 1:
                table.item(i, j).setBackground(QColor(192, 192, 192))
            elif i == 2:
                table.item(i, j).setBackground(QColor(210, 105, 30))
        table.verticalHeader().resizeSection(i, 210)
    table.setIconSize(QSize(200, 200))


def set_lists(res):
    balances = []
    ans_v = []
    ans_w = []
    for user in res:
        r4 = user[4]
        r3 = user[3]
        r5 = user[5]
        r6 = user[6]
        if r6 is not None:
            r6 = r6.split('.')[-1]
        if r4 is None:
            r4 = 0
        if r3 is None:
            r3 = 0
        balances.append(((r5, r6), user[0], user[1], user[2]))
        ans_w.append(((r5, r6), user[0], user[1], r4))
        ans_v.append(((r5, r6), user[0], user[1], r3))
    balances = sorted(balances, key=lambda k: k[3], reverse=True)
    ans_w = sorted(ans_w, key=lambda k: k[3], reverse=True)
    ans_v = sorted(ans_v, key=lambda k: k[3], reverse=True)
    place_in_balances = 0
    place_in_work = 0
    place_in_vikt = 0
    for i in range(len(balances)):
        if balances[i][1] == USER_ID:
            place_in_balances = i + 1
            break
    for i in range(len(ans_w)):
        if ans_w[i][1] == USER_ID:
            place_in_work = i + 1
            break
    for i in range(len(ans_v)):
        if ans_v[i][1] == USER_ID:
            place_in_vikt = i + 1
            break
    return (balances, ans_w, ans_v, place_in_balances, place_in_work, place_in_vikt)


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
        file = 'acc_icon.png'
        if USER_ID != -1:
            res = cur.execute("""SELECT profile_pic, balance, filename FROM users
                                    WHERE id = ?""", (USER_ID,)).fetchall()[0]
            connect.close()
            if len(res) != 0:
                if res[0] is not None:
                    file = res[0]
                if res[1] is not None:
                    self.balance_curr_txt.setText(str(res[1]))
        if file == 'acc_icon.png':
            self.acc.setIcon(QIcon(file))
        else:
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(file, res[2].split('.')[-1])
            self.icon = QIcon()
            self.icon.addPixmap(self.pixmap)
            self.acc.setIcon(self.icon)
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
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()
        MODE = self.sender().text()

    def open_shop(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return

    def open_top(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.top_w = TopWindow()
        self.top_w.setStyleSheet(stylesheet_top)
        self.top_w.show()
        self.close()

    def enter_promo(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.promo_w = PromoWindow()
        self.promo_w.setStyleSheet(stylesheet_promo)
        self.promo_w.show()
        self.close()

    def play_vikt(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.vikt = ViktWindow()
        self.vikt.setStyleSheet(stylesheet_vikt)
        self.vikt.show()
        self.close()


class TopWindow(QMainWindow, Ui_TopWindow):
    def __init__(self):
        global PLACE_IN_TOP
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.search_btn.clicked.connect(self.my_top)
        self.con = sqlite3.connect('users_db.sqlite3')
        self.cur = self.con.cursor()
        res = self.cur.execute(f"""SELECT id, username, balance, ans_vikt, ans_work, profile_pic,
         filename FROM users""").fetchall()
        tmp_res = set_lists(res)[:3]
        self.tableBalances.setColumnCount(4)
        self.tableVikt.setColumnCount(4)
        self.tableWork.setColumnCount(4)
        self.tableBalances.setRowCount(0)
        self.tableVikt.setRowCount(0)
        self.tableWork.setRowCount(0)
        self.tableBalances.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя', 'Баланс'])
        self.tableVikt.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя',
                                                  'Кол-во отвеченных вопросов'])
        self.tableWork.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя',
                                                  'Кол-во решенных загадок'])
        set_table(tmp_res[0], self.tableBalances)
        set_table(tmp_res[2], self.tableVikt)
        set_table(tmp_res[1], self.tableWork)
        self.tableTop.currentChanged.connect(self.change_state)
        self.change_state()
        self.request_txt.clear()

    def back(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()

    def change_state(self):
        if self.tableTop.currentIndex() == 3:
            self.request_txt.setEnabled(True)
        else:
            self.request_txt.setEnabled(False)

    def my_top(self):
        if self.tableTop.currentIndex() != 3:
            error('Переключитесь на вкладку "СВОЙ ТОП"!', self)
            return
        fl = False
        if self.request_txt.toPlainText() == '':
            fl = True
        try:
            if not fl:
                zaprosy = self.request_txt.toPlainText().rstrip('\n').split('\n')
                res = self.cur.execute(f"""SELECT id, username, balance, ans_vikt, ans_work, 
profile_pic, filename FROM users WHERE {" and ".join(zaprosy)}""").fetchall()
            else:
                res = self.cur.execute(f"""SELECT id, username, balance, ans_vikt, ans_work, 
profile_pic, filename FROM users""").fetchall()
            self.itog = []
            for user in res:
                r4 = user[4]
                r3 = user[3]
                r5 = user[5]
                r6 = user[6]
                if r6 is not None:
                    r6 = r6.split('.')[-1]
                if r4 is None:
                    r4 = 0
                if r3 is None:
                    r3 = 0
                self.itog.append(((r5, r6), user[0], user[1], user[2], r3, r4))
            self.tableMyTop.setColumnCount(6)
            self.tableMyTop.setRowCount(0)
            self.tableMyTop.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя', 'Баланс',
                                                          'Вопросы', 'Загадки'])
            set_table(self.itog, self.tableMyTop)
        except Exception as e:
            error(f'Возникла ошибка: {e}. Перепроверьте запрос.', self)


class PromoWindow(QMainWindow, Ui_PromoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.check_btn_2.clicked.connect(self.run)
        self.go_back.clicked.connect(self.back)

    def back(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()

    def run(self):
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        res = cur.execute("""SELECT entered, balance, promocodes FROM users
                                        WHERE id = ?""", (USER_ID,)).fetchall()[0]
        summ = random.randint(200, 1000)
        pr = self.answ_area_2.text()
        if res[0] is None:
            if res[2] is None:
                error('Вы ввели недействительный промокод!', self)
                return
            all_promos = res[2].split(';')
            if pr in all_promos:
                cur.execute(f"""UPDATE users SET entered = '{pr}', balance = {res[1] + summ} 
                            WHERE id = {USER_ID}""")
            else:
                error('Вы ввели недействительный промокод!', self)
                return
        else:
            all_entered = res[0].split(';')
            if res[2] is None:
                error('Вы ввели недействительный промокод!', self)
                return
            all_promos = res[2].split(';')
            if pr in all_promos and pr not in all_entered:
                all_entered_res = [pr, all_entered] if isinstance(all_entered, str) else \
                    [pr] + all_entered
                all_entered_res2 = ";".join(all_entered_res)
                cur.execute(f"""UPDATE users SET entered = '{all_entered_res2}', balance = 
        {res[1] + summ} WHERE id = {USER_ID}""")
            elif pr in all_promos and pr in all_entered:
                error('Вы вводили этот промокод ранее!', self)
                return
            else:
                error('Вы ввели недействительный промокод!', self)
                return
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f'На ваш баланс зачислено {summ} монеток!')
        msg.setWindowTitle("Зачисление")
        msg.exec()
        connect.commit()
        connect.close()


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
            curr_info = cur.execute(f"""SELECT balance, ans_vikt FROM users WHERE id = 
{USER_ID}""").fetchall()[0]
            ans_v = curr_info[1]
            if ans_v is None:
                ans_v = 0
            cur.execute(f"""UPDATE users SET balance = {add_s + curr_info[0]},
             ans_vikt = {ans_v + 1} WHERE id = {USER_ID}""")
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
        connect.close()

    def back(self):
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    def run(self):
        try:
            check_stavka(self.stavka_summ.text(), USER_ID)
            summ = int(self.stavka_summ.text())
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


class SlotWindow(QMainWindow, Ui_SlotWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.run_btn.clicked.connect(self.run)
        self.coef_txt.clear()
        self.win_txt.clear()
        self.fruits_txt.clear()
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        curr_blc = cur.execute(f"""SELECT balance FROM users WHERE id = 
{USER_ID}""").fetchall()[0][0]
        self.curr_txt.setText(str(curr_blc))
        self.stavka_summ.clear()
        self.curr_hard.setText(HARD_LVL)
        connect.close()

    def back(self):
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    def run(self):
        try:
            check_stavka(self.stavka_summ.text(), USER_ID)
            summ = int(self.stavka_summ.text())
            num = 9
            if HARD_LVL == 'СРЕДНЯЯ':
                num = 11
            elif HARD_LVL == 'СЛОЖНАЯ':
                num = 13
            emoji1 = random.randint(0, num)
            emoji2 = random.randint(0, num)
            emoji3 = random.randint(0, num)
            emoji4 = random.randint(0, num)
            emojis_all = {emoji4, emoji2, emoji3, emoji1}
            coef = 1
            if len(emojis_all) == 4:
                coef = 0
            if HARD_LVL == 'ЛЕГКАЯ':
                if len(emojis_all) == 3:
                    coef = 2
                elif len(emojis_all) == 2:
                    if emoji1 == emoji2 and emoji4 == emoji3 or \
                            emoji1 == emoji3 and emoji2 == emoji4 or \
                            emoji1 == emoji4 and emoji2 == emoji3:
                        coef = 6
                    else:
                        coef = 10
                elif len(emojis_all) == 1:
                    coef = 20
            elif HARD_LVL == 'СРЕДНЯЯ':
                if len(emojis_all) == 3:
                    coef = 3
                elif len(emojis_all) == 2:
                    if emoji1 == emoji2 and emoji4 == emoji3 or \
                            emoji1 == emoji3 and emoji2 == emoji4 or \
                            emoji1 == emoji4 and emoji2 == emoji3:
                        coef = 10
                    else:
                        coef = 50
                elif len(emojis_all) == 1:
                    coef = 80
            elif HARD_LVL == 'СЛОЖНАЯ':
                if len(emojis_all) == 3:
                    coef = 4
                elif len(emojis_all) == 2:
                    if emoji1 == emoji2 and emoji4 == emoji3 or \
                            emoji1 == emoji3 and emoji2 == emoji4 or \
                            emoji1 == emoji4 and emoji2 == emoji3:
                        coef = 20
                    else:
                        coef = 100
                elif len(emojis_all) == 1:
                    coef = 200
            self.fruits_txt.setText(f'=={EMOJIS[emoji1]}{EMOJIS[emoji2]}{EMOJIS[emoji3]}\
{EMOJIS[emoji4]}==')
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
        elif MODE == 'Слоты':
            self.slot_w = SlotWindow()
            self.slot_w.setStyleSheet(stylesheet_slot)
            self.slot_w.show()
        elif MODE == 'Краш-казино':
            self.crash_w = CrashKazWindow()
            self.crash_w.setStyleSheet(stylesheet_crash)
            self.crash_w.show()
        self.close()


class CrashKazWindow(QMainWindow, Ui_CrashKazWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.run_btn.clicked.connect(self.run)
        self.end_btn.clicked.connect(self.end)
        self.coef_txt.clear()
        self.win_txt.clear()
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        curr_blc = cur.execute(f"""SELECT balance FROM users WHERE id = 
{USER_ID}""").fetchall()[0][0]
        self.curr_txt.setText(str(curr_blc))
        self.stavka_summ.clear()
        self.curr_hard.setText(HARD_LVL)
        connect.close()
        self.started = False
        self.curr_coef = 1.0
        self.stavka_summ.setEnabled(True)
        self.n = 0

    def back(self):
        if self.started:
            error('Вы не завершили игру!', self)
            return
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    def run(self):
        try:
            check_stavka(self.stavka_summ.text(), USER_ID)
            ver = random.randint(0, 1000)
            coef = 0
            tmp = self.coef_txt.text()
            if tmp != '':
                if HARD_LVL == 'ЛЕГКАЯ':
                    if ver < 700:
                        coef = random.randint(5, 10) / 100
                    elif ver < 997:
                        coef = -1 * random.randint(1, 5) / 100
                elif HARD_LVL == 'СРЕДНЯЯ':
                    if ver < 500:
                        coef = random.randint(10, 20) / 100
                    elif ver < 997:
                        coef = -1 * random.randint(1, 10) / 100
                elif HARD_LVL == 'СЛОЖНАЯ':
                    if ver < 300:
                        coef = random.randint(20, 30) / 100
                    elif ver < 997:
                        coef = -1 * random.randint(5, 15) / 100
                if ver >= 998:
                    coef = -1000000000
            old_coef = round(self.curr_coef, 2)
            new_coef = round(self.curr_coef + coef, 2)
            self.curr_coef = new_coef
            if new_coef < old_coef:
                self.coef_txt.setText(f'x{str(new_coef)} \
(\U0001F4C9-x{str(old_coef - new_coef)[:4]})')
            else:
                self.coef_txt.setText(f'x{str(new_coef)} \
(\U0001F4C8+x{str(new_coef - old_coef)[:4]})')
            if self.curr_coef <= 0:
                self.started = False
                self.coef_txt.clear()
                self.win_txt.clear()
                self.stavka_summ.setEnabled(True)
                self.curr_coef = 1
                self.n = 0
                error('Игра заверешена, т.к. коэффициент опустился или стал равен 0.', self)
                return
            self.started = True
            self.stavka_summ.setEnabled(False)
            self.n += 1
        except Exception as e:
            error(e, self)

    def end(self):
        if self.n == 1:
            error('Нельзя завершать игру на первом шаге!', self)
            return
        if not self.started:
            return
        try:
            summ = int(self.stavka_summ.text())
            coef = self.curr_coef
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
            self.started = False
            self.stavka_summ.setEnabled(True)
            self.curr_coef = 1.0
            self.n = 0
        except Exception as e:
            error(e, self)


class ProbSolvWindow(QMainWindow, Ui_ProbSolvWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.check_btn.clicked.connect(self.check_ans)
        self.ind = -1
        self.upd()
        self.promo_txt.hide()
        self.label.hide()

    def back(self):
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    def check_ans(self):
        self.label.hide()
        self.promo_txt.hide()
        msg = QMessageBox(self)
        if self.answ_area.text() == WORK_Q[HARD_LVL.lower().capitalize()][self.ind][1]:
            add_s = 100
            if HARD_LVL == 'СРЕДНЯЯ':
                add_s = 300
            elif HARD_LVL == 'СЛОЖНАЯ':
                add_s = 600
            ver = random.randint(0, 2)
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
            res = cur.execute(f"""SELECT balance, promocodes, ans_work FROM users WHERE id = 
{USER_ID}""").fetchall()[0]
            curr_blc = res[0]
            user_promos = res[1]
            ans_w = res[2]
            if ans_w is None:
                ans_w = 0
            if ver == 0:
                self.label.show()
                curr_promo = random.choice(CODES)
                if user_promos is not None:
                    if isinstance(user_promos, str):
                        while curr_promo == user_promos:
                            curr_promo = random.choice(CODES)
                    else:
                        while curr_promo in user_promos:
                            curr_promo = random.choice(CODES)
                    res1 = ";".join([curr_promo, user_promos] if isinstance(user_promos, str)
                                    else user_promos + [curr_promo])
                    cur.execute(f"""UPDATE users SET balance = {add_s + curr_blc},
                                    promocodes = '{res1}', ans_work = {ans_w + 1} WHERE id = 
{USER_ID}""")
                else:
                    cur.execute(f"""UPDATE users SET balance = {add_s + curr_blc}, 
                    promocodes = '{curr_promo}', ans_work = {ans_w + 1} WHERE id = {USER_ID}""")
                self.promo_txt.setText(curr_promo)
                self.promo_txt.show()
            else:
                cur.execute(f"""UPDATE users SET balance = {add_s + curr_blc}, ans_work = 
{ans_w + 1} WHERE id = {USER_ID}""")
            connect.commit()
            connect.close()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f'Верный ответ! Вы заработали: {add_s} монеток!')
            msg.setWindowTitle("Круто!")
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
        global ACC_OBJ
        super().__init__()
        self.setupUi(self)
        ACC_OBJ = self
        self.setFixedSize(1920, 1100)
        self.psw_btn.clicked.connect(self.show_hide)
        self.go_back.clicked.connect(self.open_choice_win)
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        res = cur.execute("""SELECT * FROM users
                        WHERE id = ?""", (USER_ID,)).fetchall()
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
        self.del_acc_btn.clicked.connect(self.confirm_del)
        pic = res[0][4]
        self.pixmap = QPixmap()
        if pic is not None:
            self.pixmap.loadFromData(pic, res[0][5].split('.')[-1])
            self.image = QLabel(self)
            self.image.setPixmap(self.pixmap)
            self.image.setScaledContents(True)
            self.image.move(240, 170)
            self.image.resize(200, 200)
            self.txt_ava = QLabel('Ваша аватарка', self)
            self.txt_ava.move(240, 365)
            self.txt_ava.setStyleSheet('color: rgb(0, 0, 0)')
        res = cur.execute(f"""SELECT id, username, balance, ans_vikt, ans_work, profile_pic,
                 filename FROM users""").fetchall()
        places = set_lists(res)[3:] #w,v
        self.place_txt.setText(f'Место среди балансов: #{places[0]}\nСреди решенных загадок: \
#{places[1]}\nСреди ответов на вопросы в викторине: #{places[2]}')
        connect.close()

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

    def confirm_del(self):
        self.confirm = YesNoDialog()
        self.confirm.show()

    def del_acc(self):
        global LOGINED, USER_ID
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


class YesNoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Запрос удаления")
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.addButton('Да', QDialogButtonBox.ButtonRole.AcceptRole)
        self.buttonBox.addButton('Нет', QDialogButtonBox.ButtonRole.RejectRole)
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.rejected)

        self.layout = QVBoxLayout()
        message = QLabel("Вы действительно хотите удалить аккаунт?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def rejected(self):
        self.close()

    def accepted(self):
        AccWindow.del_acc(ACC_OBJ)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    sys.exit(app.exec())
