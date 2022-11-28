import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QLabel, QLineEdit
from PyQt6.QtWidgets import QInputDialog, QTableWidgetItem, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap, QIcon, QColor
from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
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
from shop import *
from invent import *


# === ОБЪЯВЛЯЕМ КОНСТАНТЫ ДЛЯ РАБОТЫ ПРОГРАММЫ ===
LOGINED = False
USER_ID = -1
ACC_OBJ = None
MODE = None
HARD_LVL = None
EMOJIS = ['\U0001F95D', '\U0001F34E', '\U0001F351', '\U0001F34F', '\U0001F350', '\U0001F353',
          '\U0001F34C', '\U0001F34A', '\U0001F34B', '\U0001F349', '\U0001F347', '\U0001F352',
          '\U0001F34D', '\U0001F348']


# === ФУНКЦИЯ ВЫВОДА ОШИБКИ ===
def error(exp, self):
    # exp - либо класс ошибки, либо строка (если ошибка может возникнуть всего 1 раз)
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setText(str(exp))
    msg.setWindowTitle("Ошибка")
    msg.exec()


# === ФУНКЦИЯ ДОБАВЛЕНИЯ ЮЗЕРА В БД ===
def append_user(name, psw):
    connect = sqlite3.connect('users_db.sqlite3')
    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO users(username, password, balance) VALUES('{name}', '{psw}', 0)")
    connect.commit()
    id = cursor.execute(f"""SELECT id FROM users WHERE username = '{name}' and
password = '{psw}'""").fetchall()[-1][-1]
    connect.close()
    return id


# === ФУНКЦИЯ НАСТРОЙКИ ТАБЛИЦ ТОПА ===
def set_table(array, table):
    # array - двумерный-список (таблица), table - экземпляр класса tableWidget
    for i, row in enumerate(array):
        table.setRowCount(table.rowCount() + 1)
        for j, elem in enumerate(row):
            # Если аватарака не установлена, добавляем в ячейку текст об этом
            if j == 0 and elem[0] is None:
                table.setItem(i, j, QTableWidgetItem('Нет аватарки'))
                if i == 0:
                    table.item(i, j).setBackground(QColor(255, 215, 0))
                elif i == 1:
                    table.item(i, j).setBackground(QColor(192, 192, 192))
                elif i == 2:
                    table.item(i, j).setBackground(QColor(210, 105, 30))
                continue
            elif j == 0 and elem[0] is not None:
                # Если аватарка есть, то делаем магию:
                pixmap = QPixmap()
                pixmap.loadFromData(elem[0], elem[1])
                # elem[0] - файл из БД, имеющий тип BLOB, elem[1] - расширение картинки
                # (png, jpg...)
                icon = QIcon()
                icon.addPixmap(pixmap)
                item = QTableWidgetItem(icon, '')
                table.setItem(i, j, item)
                table.horizontalHeader().resizeSection(j, 210)
                # Настраиваем размеры аватарки
            else:
                # Сюда попадаем, если мы находимя не в ячейке, содержащей аватарку
                table.setItem(i, j, QTableWidgetItem(str(elem)))
                table.horizontalHeader().resizeSection(j, 245)
            # Для первых 3 человек делаем строки цветными
            if i == 0:
                table.item(i, j).setBackground(QColor(255, 215, 0))
            elif i == 1:
                table.item(i, j).setBackground(QColor(192, 192, 192))
            elif i == 2:
                table.item(i, j).setBackground(QColor(210, 105, 30))
        table.verticalHeader().resizeSection(i, 210)
    table.setIconSize(QSize(200, 200))


# === Ф-ИЯ СОЗДАНИЯ ПОЛЬЗОВАТЕЛЬСКОГО ТОПА: НАСТРОЙКА ТАБЛИЦЫ ===
def set_lists(res):
    # res - двумерный список, по сути, вся БД с нужными столбцами
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
        # r5 - ава (тип BLOB), r6 - расширение авы, r3 - кол-во отвеченных вопросов,
        # r4 - кол-во решенных загадок, user[2] - баланс юзера
        # user[0] - id юзера, user[1] - имя юзера
        balances.append(((r5, r6), user[0], user[1], user[2]))
        ans_w.append(((r5, r6), user[0], user[1], r4))
        ans_v.append(((r5, r6), user[0], user[1], r3))
    balances = sorted(balances, key=lambda k: k[3], reverse=True)
    ans_w = sorted(ans_w, key=lambda k: k[3], reverse=True)
    ans_v = sorted(ans_v, key=lambda k: k[3], reverse=True)
    place_in_balances = 0
    place_in_work = 0
    place_in_vikt = 0
    # Получив отсортированные списки, ищем места юзера в них
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
    # Возвращаем универсальный кортеж - первая половина нужна для настройки tableWidget,
    # а вторая - для отображения инфы на странице юзера
    return (balances, ans_w, ans_v, place_in_balances, place_in_work, place_in_vikt)


# === Ф-ИЯ ПОЛУЧЕНИЯ БАЛАНСА И ПРОВЕРКИ ИНВЕНТАРЯ НА НАЛИЧИЕ ПРЕМИУМА ===
def get_balance_and_premium_coef():
    con = sqlite3.connect('users_db.sqlite3')
    cur = con.cursor()
    res = cur.execute(f"""SELECT balance, inventory FROM users WHERE id = 
    {USER_ID}""").fetchall()[0]
    blc = res[0]
    invent1 = check_premium(res[1])
    return (blc, invent1)


# === КЛАСС ОСНОВГО ОКНА ===
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.pushButton.clicked.connect(self.games)

    # === Ф-ИЯ ДЛЯ ПЕРЕХОДА НА ОКНО С ИГРАМИ ===
    def games(self):
        self.games_w = ChoiceWindow()
        # Настраиваем affordable design для нашего окошка :))
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()


# === КЛАСС ОКНА С ИГРАМИ ===
class ChoiceWindow(QMainWindow, Ui_ChoiceWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        file = 'acc_icon.png'
        # Если юзер уже залогинился, то проверяем, есть ли у него ава (соотв. и выводим его баланс)
        if USER_ID != -1:
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
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
            # This magic я поисал выше...
            self.pixmap.loadFromData(file, res[2].split('.')[-1])
            self.icon = QIcon()
            self.icon.addPixmap(self.pixmap)
            self.acc.setIcon(self.icon)
        self.acc.setIconSize(QSize(50, 50))
        # Можете скипнуть, ничего интересного - коннектим кнопки к функциям
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

    # === Ф-ИЯ ОТКРЫТИЯ ПРОФИЛЯ, ЛИБО ВХОДА/РЕГИСТРАЦИИ ===
    def info(self):
        if not LOGINED:
            self.rol_w = LogOrRegWindow()
            # Affordable design... все цвета, что есть здесь - модные!!!
            self.rol_w.setStyleSheet(stylesheet_rol)
            self.rol_w.show()
            self.close()
        else:
            self.acc_w = AccWindow()
            self.acc_w.setStyleSheet(stylesheet_acc)
            self.acc_w.show()
            self.close()

    # === Ф-ИЯ ОТКРЫТИЯ ПРЕДЫДУЩЕГО ПО ЛОГИКЕ ОКНА === (данную ф-ию дальше я комментарировать не
    # буду, и так все ясно... Правда ведь?)
    def back(self):
        self.main_w = MainWindow()
        self.main_w.setStyleSheet(stylesheet_main)
        self.main_w.show()
        self.close()

    # === Ф-ИЯ ОТКРЫТИЯ ВЫБОРА СЛОЖНОСТИ (ДЛЯ 4 КНОПОК ОДНА) ===
    def choose_lvl(self):
        global MODE
        # Сначала дайте нам логин и пароль, потом уже поговорим...
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()
        # Запоминаем выбранный режим
        MODE = self.sender().text()

    # === Ф-ИЯ ОТКРЫТИЯ МАГАЗИНА ===
    def open_shop(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.shop_w = ShopWindow()
        self.shop_w.setStyleSheet(stylesheet_shop)
        self.shop_w.show()
        self.close()

    # === Ф-ИЯ ОТКРЫТИЯ ТОПА ===
    def open_top(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.top_w = TopWindow()
        self.top_w.setStyleSheet(stylesheet_top)
        self.top_w.show()
        self.close()

    # === Ф-ИЯ ОТКРЫТИЯ ОКНА С ВВОДОМ ПРОМОКОДА ===
    def enter_promo(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.promo_w = PromoWindow()
        self.promo_w.setStyleSheet(stylesheet_promo)
        self.promo_w.show()
        self.close()

    # === Ф-ИЯ ОТКРЫТИЯ ВИКТОРИНЫ ===
    def play_vikt(self):
        if USER_ID == -1:
            error('Сначала нужно зарегистрироваться или войти в свой аккаунт!', self)
            return
        self.vikt = ViktWindow()
        self.vikt.setStyleSheet(stylesheet_vikt)
        self.vikt.show()
        self.close()


# === КЛАСС ОКНА ВЫБОРА СЛОЖНОСТИ ===
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

    # === Ф-ИЯ ДАЛЬНЕЙШЕГО ВЫБОРА ОКНА ===
    def run(self):
        global HARD_LVL
        HARD_LVL = self.sender().text()
        # HARD_LVL - текст названия сложности
        # В зависимости от сложности выбираем игру
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


# === КЛАСС ОКНА С ТОПОМ ===
class TopWindow(QMainWindow, Ui_TopWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.search_btn.clicked.connect(self.my_top)
        self.tableTop.currentChanged.connect(self.change_state)
        # Чистим поле (если окно открывается не первый раз
        self.request_txt.clear()
        # Подключаемся к БД, чтобы взять нужную инфу о юзере
        self.con = sqlite3.connect('users_db.sqlite3')
        self.cur = self.con.cursor()
        res = self.cur.execute(f"""SELECT id, username, balance, ans_vikt, ans_work, profile_pic,
         filename FROM users""").fetchall()
        # Как я и писал выше, set_lists возвращает универсальный кортеж, поэтому нужно взять срез
        tmp_res = set_lists(res)[:3]
        # Настраиваем таблицы: указываем кол-во столбцов и строк, названия столбцов...
        self.tableBalances.setColumnCount(4)
        self.tableVikt.setColumnCount(4)
        self.tableWork.setColumnCount(4)
        self.tableBalances.setRowCount(0)
        self.tableVikt.setRowCount(0)
        self.tableWork.setRowCount(0)
        self.tableBalances.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя', 'Баланс'])
        self.tableVikt.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя',
                                                  'Ответов на вопросы'])
        self.tableWork.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя',
                                                  'Решений загадок'])
        # Используем ф-ию настройки tableWidget
        set_table(tmp_res[0], self.tableBalances)
        set_table(tmp_res[2], self.tableVikt)
        set_table(tmp_res[1], self.tableWork)
        # Об этой ф-ии написано ниже
        self.change_state()

    def back(self):
        self.con.close()
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()

    # === Ф-ИЯ ИЗМ. СОСТОЯНИЯ ТЕКСТ. ПОЛЯ ===
    # Ввод в текст. поле доступен только, если выбрана вкладка "СВОЙ ТОП". Делаем соотв. настройки
    def change_state(self):
        if self.tableTop.currentIndex() == 3:
            # Если вкладка выбрана, то писать можно...
            self.request_txt.setEnabled(True)
        else:
            self.request_txt.setEnabled(False)

    # === Ф-ИЯ ИЗМ. СОСТОЯНИЯ ТЕКСТ. ПОЛЯ ===
    def my_top(self):
        # Ввод в текст. поле доступен только, если выбрана вкладка "СВОЙ ТОП". Делаем соотв.
        # настройки
        if self.tableTop.currentIndex() != 3:
            error('Переключитесь на вкладку "СВОЙ ТОП"!', self)
            return
        fl = False
        if self.request_txt.toPlainText() == '':
            fl = True
        try:
            # Если ввод не пустой, то формируем запрос в БД для получения нужных данных
            if not fl:
                zaprosy = self.request_txt.toPlainText().rstrip('\n').split('\n')
                res = self.cur.execute(f"""SELECT id, username, balance, ans_vikt, ans_work, 
profile_pic, filename FROM users WHERE {" and ".join(zaprosy)}""").fetchall()
            else:
                # Иначе просто берем все колонки
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
                # r5 - ава (тип BLOB), r6 - расширение авы, r3 - кол-во отвеченных вопросов,
                # r4 - кол-во решенных загадок, user[2] - баланс юзера
                # user[0] - id юзера, user[1] - имя юзера
                self.itog.append(((r5, r6), user[0], user[1], user[2], r3, r4))
            self.tableMyTop.setColumnCount(6)
            self.tableMyTop.setRowCount(0)
            self.tableMyTop.setHorizontalHeaderLabels(['Аватарка', 'ID', 'Имя', 'Баланс',
                                                       'Вопросы', 'Загадки'])
            set_table(self.itog, self.tableMyTop)
        except Exception as e:
            error(f'Возникла ошибка: {e}. Перепроверьте запрос.', self)


# === КЛАСС ОКНА ДЛЯ ВВОДА ПРОМОКОДА ===
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

    # === Ф-ИЯ ДЛЯ ПРОВЕРКИ ПРОМОКОДА (БЫЛ ЛИ ВВЕДЕН И СУЩЕСТВУЕТ ЛИ (С УСЛОВИЕМ, ЕСЛИ ЮЗЕР ЕГО
    # ПОЛУЧИЛ РАНЕЕ)) ===
    def run(self):
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        # Подключаемся к БД
        res = cur.execute("""SELECT entered, balance, promocodes FROM users
                                        WHERE id = ?""", (USER_ID,)).fetchall()[0]
        summ = random.randint(1000, 10000)
        pr = self.answ_area_2.text()
        # Проверяем промокод: 1) Существует ли он (был ли получен раньше)
        # 2) Если он есть в списке введенных, то вызываем исключение
        # 3) Иначе добавляем его в список введенных и начисляем сумму на баланс
        # all_promos - список всех полученных промокод
        # pr - промокод, который надо проверить
        # all_entered_promos - список всех ранее введенных промокодов

        # res[0] - строка с разделителем ';' всех промокодов, которые уже вводили
        # res[1] - баланс, res[2] - все полученные промокоды
        if res[0] is None:
            # Проверяем, вводили ли вообще промокоды раньше
            if res[2] is None:
                # Если юзер не получал промокоды, вызываем исключение
                error('Вы ввели недействительный промокод!', self)
                return
            all_promos = res[2].split(';')
            # Проверяем, есть ли промокод во введенных
            if pr in all_promos:
                # res[1] - баланс, res[2] - все полученные промокоды
                cur.execute(f"""UPDATE users SET entered = '{pr}', balance = {res[1] + summ} 
                            WHERE id = {USER_ID}""")
            else:
                error('Вы ввели недействительный промокод!', self)
                return
        else:
            # Делаем все аналогично, но проверяем дополнительно, что промокода нет в ранее
            # введенных
            all_entered = res[0].split(';')
            if res[2] is None:
                error('Вы ввели недействительный промокод!', self)
                return
            # Способ хранения промокодов - через спец. разделитель
            all_promos = res[2].split(';')
            if pr in all_promos and pr not in all_entered:
                all_entered_res = [pr, all_entered] if isinstance(all_entered, str) else \
                    [pr] + all_entered
                all_entered_res2 = ";".join(all_entered_res)
                # Если все ок, пополняем баланс
                cur.execute(f"""UPDATE users SET entered = '{all_entered_res2}', balance = 
        {res[1] + summ} WHERE id = {USER_ID}""")
            elif pr in all_promos and pr in all_entered:
                error('Вы вводили этот промокод ранее!', self)
                return
            else:
                error('Вы ввели недействительный промокод!', self)
                return
        # выводим сообщение об успешной активации
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f'На ваш баланс зачислено {summ} монеток!')
        msg.setWindowTitle("Зачисление")
        msg.exec()
        connect.commit()
        connect.close()


# === КЛАСС ОКНА ДЛЯ ВИКТОРИНЫ ===
class ViktWindow(QMainWindow, Ui_ViktWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.check_btn.clicked.connect(self.check_ans)
        self.tip_btn.clicked.connect(self.tip_show)
        # Создаем индекс вопроса (для того, чтобы потом не было 2 вопроса одинаковых подряд)
        self.ind = -1
        # Обновляем задание
        self.upd()

    def back(self):
        self.ch_w = ChoiceWindow()
        self.ch_w.setStyleSheet(stylesheet_choice)
        self.ch_w.show()
        self.close()

    # === Ф-ИЯ ПРОВЕРКИ ОТВЕТА ===
    def check_ans(self):
        msg = QMessageBox(self)
        # Если ответ верный, начисляем деньги
        if self.answ_area.text().lower() == VIKT_A[self.ind].lower():
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
            # Берем из БД нужны данные: баланс, кол-во ответов и инвентарь (чекаем премиум)
            curr_info = cur.execute(f"""SELECT balance, ans_vikt, inventory FROM users WHERE id = 
{USER_ID}""").fetchall()[0]
            ans_v = curr_info[1]  # кол-во ответов
            invent1 = check_premium(curr_info[-1])  # чекаем на наличие премиума
            if ans_v is None:
                ans_v = 0
            add_s = 5000
            msg.setIcon(QMessageBox.Icon.Information)
            vyighysh = add_s * invent1
            msg.setText(f'Верный ответ! Вы заработали: {int(vyighysh)} монеток!')
            msg.setWindowTitle("Круто!")
            cur.execute(f"""UPDATE users SET balance = {int(vyighysh + curr_info[0])},
             ans_vikt = {ans_v + 1} WHERE id = {USER_ID}""")
            connect.commit()
            connect.close()
            self.upd()
        else:
            # Иначе выводим грустное сообщение
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText('Неверный ответ!')
            msg.setWindowTitle("Жаль!")
        msg.exec()

    # === Ф-ИЯ ВЫВОДА ПОДСКАЗКИ ===
    def tip_show(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(VIKT_T.get(self.ind, 'Подсказки на данный вопрос нет.'))
        msg.setWindowTitle("Tip")
        msg.exec()

    # === Ф-ИЯ ОБНОВЛЕНИЯ ВОПРОСА ===
    def upd(self):
        ind2 = self.ind
        while self.ind == ind2:
            self.ind = random.randint(1, 72)
        if self.ind in PHOTOS_VIKT:
            self.image_w = QWidget()
            self.image = QLabel(self.image_w)
            self.image.setPixmap(QPixmap(PHOTOS_VIKT[self.ind]))
            self.image.move(0, 0)
            self.image.resize(self.image.sizeHint())
            self.image_w.resize(self.image.sizeHint())
            self.image_w.show()
            self.image_w.move(0, 0)
        self.task_txt.setText(VIKT_Q[self.ind])
        self.answ_area.clear()


# === КЛАСС ОКНА КАЗИНО ===
class KazWindow(QMainWindow, Ui_KazWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.run_btn.clicked.connect(self.run)
        self.coef_txt.clear()
        self.win_txt.clear()
        self.stavka_summ.clear()
        self.curr_hard.setText(HARD_LVL)
        self.connect = sqlite3.connect('users_db.sqlite3')
        self.cur = self.connect.cursor()
        # Берем из БД баланс юзера
        curr_blc = self.cur.execute(f"""SELECT balance FROM users WHERE id = 
{USER_ID}""").fetchall()[0][0]
        self.curr_txt.setText(str(curr_blc))
        # Устанавливаем сложность

    def back(self):
        self.connect.close()
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    # === Ф-ИЯ ВЫВОДА КОЭФФ. И ПОПОЛНЕНИЯ БАЛАНСА ===
    def run(self):
        try:
            # Получаем баланс и инвентарь юзера
            data = get_balance_and_premium_coef()
            curr_blc = data[0]
            invent1 = data[-1]
            # Проверяем корректность ставки
            check_stavka(self.stavka_summ.text(), USER_ID)
            summ = int(self.stavka_summ.text())
            ver = random.randint(0, 10000)
            coef = 1
            # В зависимости от уровня сложности выбираем коэф.
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
            vyighysh = summ * coef * invent1
            self.win_txt.setText(str(vyighysh))
            # Очевидно - пополняем баланс
            self.cur.execute(f"""UPDATE users SET balance = {int(curr_blc + vyighysh - 
                                                            summ)} WHERE id = {USER_ID}""")
            self.connect.commit()
            self.curr_txt.setText(str(int(curr_blc + vyighysh - summ)))
        except Exception as e:
            error(e, self)


# === КЛАСС ОКНА СЛОТОВ ===
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
        self.stavka_summ.clear()
        self.curr_hard.setText(HARD_LVL)
        # Можно не комментировать? И так понятно же все: предустанавливаем начальные настройки
        self.connect = sqlite3.connect('users_db.sqlite3')
        self.cur = self.connect.cursor()
        curr_blc = self.cur.execute(f"""SELECT balance FROM users WHERE id = 
{USER_ID}""").fetchall()[0][0]
        self.curr_txt.setText(str(curr_blc))

    def back(self):
        self.connect.close()
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    # === КЛАСС ОКНА КАЗИНО ===
    def run(self):
        try:
            data = get_balance_and_premium_coef()
            curr_blc = data[0]
            invent1 = data[-1]
            check_stavka(self.stavka_summ.text(), USER_ID)
            summ = int(self.stavka_summ.text())
            num = 9
            # В зависимости от сложности выбираем кол-во фруктов
            if HARD_LVL == 'СРЕДНЯЯ':
                num = 11
            elif HARD_LVL == 'СЛОЖНАЯ':
                num = 13
            emoji1 = random.randint(0, num)
            emoji2 = random.randint(0, num)
            emoji3 = random.randint(0, num)
            emoji4 = random.randint(0, num)
            # Рандомно выбираем фрукты
            emojis_all = {emoji4, emoji2, emoji3, emoji1}
            coef = 1
            if len(emojis_all) == 4:
                coef = 0
            # В зависимости от сложности выбираем коэф.
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
            vyighysh = summ * coef * invent1
            self.win_txt.setText(str(int(vyighysh)))
            # ----||----
            self.cur.execute(f"""UPDATE users SET balance = {int(curr_blc + vyighysh - 
                                                            summ)} WHERE id = {USER_ID}""")
            self.connect.commit()
            self.curr_txt.setText(str(int(curr_blc + vyighysh - summ)))
        except Exception as e:
            error(e, self)


# === КЛАСС ОКНА КРАШ-КАЗИНО ===
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
        self.stavka_summ.clear()
        self.curr_hard.setText(HARD_LVL)
        self.connect = sqlite3.connect('users_db.sqlite3')
        self.cur = self.connect.cursor()
        curr_blc = self.cur.execute(f"""SELECT balance FROM users WHERE id = 
{USER_ID}""").fetchall()[0][0]
        self.curr_txt.setText(str(curr_blc))
        # Создаем переменную, отвечающую за то, началась ли игра
        self.started = False
        self.curr_coef = 1.0
        # Т.к. игра продолжительная, то нужно запоминать текущ. коэф.
        self.stavka_summ.setEnabled(True)
        # Во время игры запрещено менять ставку!
        self.n = 0
        # Заводим переменную n - если она равна 1, то нельзя прерывать игру (отвечает за кол-во
        # шагов в игре

    def back(self):
        # Нельзя выйти из игры, не завершив ее!
        if self.started:
            error('Вы не завершили игру!', self)
            return
        self.connect.close()
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    # === Ф-ИЯ ИЗМЕНЕНИЯ КОЭФ. ===
    def run(self):
        try:
            check_stavka(self.stavka_summ.text(), USER_ID)
            ver = random.randint(0, 1000)
            coef = 0
            if self.n != 0:
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
            # Изменяем коэф., обновляем отображение данных у юзера
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
                # Если коэф. стал меньше 0, то игра должна завершиться
                self.started = False
                self.coef_txt.clear()
                self.win_txt.clear()
                self.stavka_summ.setEnabled(True)
                self.curr_coef = 1
                self.n = 0
                error('Игра завершена, т.к. коэффициент опустился или стал равен 0.', self)
                self.end()
                return
            self.started = True
            self.stavka_summ.setEnabled(False)
            self.n += 1
        except Exception as e:
            error(e, self)

    # === Ф-ИЯ ЗАВЕРШЕНИЯ ИГРЫ ===
    def end(self):
        if self.n == 1:
            error('Нельзя завершать игру на первом шаге!', self)
            return
        if not self.started:
            return
        try:
            data = get_balance_and_premium_coef()
            curr_blc = data[0]
            invent1 = data[-1]
            summ = int(self.stavka_summ.text())
            coef = self.curr_coef
            vyighysh = summ * coef * invent1
            self.win_txt.setText(str(int(vyighysh)))
            # Обновляем баланс
            self.cur.execute(f"""UPDATE users SET balance = {int(curr_blc + vyighysh - 
                                                            summ)} WHERE id = {USER_ID}""")
            self.connect.commit()
            self.curr_txt.setText(str(int(curr_blc + vyighysh - summ)))
            self.started = False
            # Заканчиваем игру и разрешаем снова писать сумму ставки
            self.stavka_summ.setEnabled(True)
            self.curr_coef = 1.0
            self.n = 0
        except Exception as e:
            error(e, self)


# === КЛАСС ОКНА КОМАНДЫ РАБОТАТЬ ===
class ProbSolvWindow(QMainWindow, Ui_ProbSolvWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.check_btn.clicked.connect(self.check_ans)
        self.promo_txt.hide()
        self.label.hide()
        # Скрываем текст промокода и задаем атрибут ind - индекс текущего вопроса
        self.ind = -1
        self.upd()

    def back(self):
        self.lvl_w = LvlWindow()
        self.lvl_w.setStyleSheet(stylesheet_lvl)
        self.lvl_w.show()
        self.close()

    # === Ф-ИЯ ПРОВЕРКИ ОТВЕТА ===
    def check_ans(self):
        self.label.hide()
        self.promo_txt.hide()
        msg = QMessageBox(self)
        if self.answ_area.text() == WORK_Q[HARD_LVL.lower().capitalize()][self.ind][1]:
            # Если ответ правильный, то исходя от сложности, задаем сумму пополнения
            add_s = 1000
            if HARD_LVL == 'СРЕДНЯЯ':
                add_s = 2000
            elif HARD_LVL == 'СЛОЖНАЯ':
                add_s = 3000
            ver = random.randint(0, 2)
            # ver - если ver = 0 (шанс 33%), то выдадим промокод
            connect = sqlite3.connect('users_db.sqlite3')
            cur = connect.cursor()
            # ПоДкЛюЧаЕмСя К БД
            res = cur.execute(f"""SELECT balance, promocodes, ans_work, inventory FROM users WHERE 
            id = {USER_ID}""").fetchall()[0]
            curr_blc = res[0]  # тек. баланс
            user_promos = res[1]  # полученные промокоды юзера
            ans_w = res[2]  # кол-во решенных загадок
            invent1 = check_premium(res[-1])
            if ans_w is None:  # Если юзер ни разу не решал загадки, то задаем значение 0
                ans_w = 0
            if ver == 0:
                self.label.show()
                curr_promo = random.choice(CODES)
                # Если юзер удачливый, то он получит промокод :>
                if user_promos is not None:
                    # Проверяем тип переменной, от чего зависит способ добавления в БД нового
                    # промокода

                    # user_promos - все промокоды юзера
                    if isinstance(user_promos, str):
                        while curr_promo == user_promos:
                            curr_promo = random.choice(CODES)
                    else:
                        while curr_promo in user_promos:
                            curr_promo = random.choice(CODES)  # curr_promo - выбранный промокод
                    res1 = ";".join([curr_promo, user_promos] if isinstance(user_promos, str)
                                    else user_promos + [curr_promo])
                    cur.execute(f"""UPDATE users SET balance = {int(add_s * invent1 + curr_blc)},
                                    promocodes = '{res1}', ans_work = {ans_w + 1} WHERE id = 
{USER_ID}""")
                else:
                    # Если юзер не получал ранее промокоды, то задаем значение, равное новому
                    # промокоду
                    cur.execute(f"""UPDATE users SET balance = {int(add_s * invent1 + curr_blc)}, 
                    promocodes = '{curr_promo}', ans_work = {ans_w + 1} WHERE id = {USER_ID}""")
                self.promo_txt.setText(curr_promo)
                self.promo_txt.show()
            else:
                # Если юзеру не повезло, просто пополняем баланс
                cur.execute(f"""UPDATE users SET balance = {int(add_s * invent1 + curr_blc)}, 
                ans_work = {ans_w + 1} WHERE id = {USER_ID}""")
            connect.commit()
            connect.close()
            # Сохраняем изменения, выводим уведомление о верном решении загадки
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f'Верный ответ! Вы заработали: {int(add_s * invent1)} монеток!')
            msg.setWindowTitle("Круто!")
            self.upd()
        else:
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText('Неверный ответ!')
            msg.setWindowTitle("Жаль!")
        msg.exec()

    # === Ф-ИЯ ОБНОВЛЕНИЯ ТЕКСТА НА ЭКРАНЕ ===
    def upd(self):
        ind2 = self.ind
        while self.ind == ind2:
            self.ind = random.randint(0, 14)
        self.task_txt.setText(WORK_Q[HARD_LVL.lower().capitalize()][self.ind][0])
        self.answ_area.clear()


# === КЛАСС ОКНА МАГАЗИНА ===
class ShopWindow(QMainWindow, Ui_ShopWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.go_back.clicked.connect(self.back)
        self.buy_btn.clicked.connect(self.buy)
        self.con = sqlite3.connect('users_db.sqlite3')
        self.cur = self.con.cursor()
        # Из БД достаем всю инфу о товарах, заносим ее в таблицу
        res = self.cur.execute(f"""SELECT * FROM list""").fetchall()
        self.tableItems.setColumnCount(3)
        self.tableItems.setRowCount(0)
        self.tableItems.setHorizontalHeaderLabels(['ID', 'Название товара', 'Стоимость'])
        for i, row in enumerate(res):
            self.tableItems.setRowCount(self.tableItems.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableItems.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableItems.horizontalHeader().resizeSection(0, 150)
        self.tableItems.horizontalHeader().resizeSection(1, 800)
        self.tableItems.horizontalHeader().resizeSection(2, 200)

    # === Ф-ИЯ ПОКУПКИ ТОВАРА ===
    def buy(self):
        # Проверка, выбрал ли юзер товар
        if not len(self.tableItems.selectedIndexes()):
            error('Вы не выбрали товар для покупки!', self)
            return
        try:
            res = self.cur.execute(f"""SELECT balance, inventory FROM users WHERE id = 
{USER_ID}""").fetchall()[0]
            blc = res[0]  # баланс
            invent1 = res[1]  # инвентарь
            ind = self.tableItems.selectedIndexes()[0].row() + 1  # индекс товара в списке предметов
            price = self.cur.execute(f"""SELECT price FROM list WHERE id = 
{ind}""").fetchall()[0][0]
            # Проверяем баланс
            if price > blc:
                raise SmallBalanceError
            if invent1 is None:
                invent1 = str(ind)
            else:
                invent1 = invent1.split(';')
                if isinstance(invent1, list):
                    if str(ind) in invent1:
                        # Нельзя купить товар два раза
                        error('Вы уже покупали данный товар!', self)
                        return
                    invent1.append(str(ind))
                elif isinstance(invent1, str):
                    if invent1 == str(ind):
                        error('Вы уже покупали данный товар!', self)
                        return
                    invent1 = [str(ind), invent1]
                else:
                    raise TypeError
            self.cur.execute(f"""UPDATE users SET balance = {blc - price}, 
inventory = {";".join(invent1)} WHERE id = {USER_ID}""")
            self.con.commit()
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Information)
            # Уведомление об успешной покупке
            msg.setText(f'Покупка совершена! Баланс: {blc - price} монеток.')
            msg.setWindowTitle("Круто!")
            msg.exec()
        except Exception as e:
            error(f'Возникла ошибка: {e}. Попробуйте выбрать товар еще раз (ВАЖНО: нужно выбрать \
1 ячейку - индекс товара!)', self)

    def back(self):
        self.con.close()
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()


# === КЛАСС ОКНА ВЫБОРА ЛОГИНА В СИСТЕМУ ===
class LogOrRegWindow(QMainWindow, Ui_LogOrRegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.reg_syst_btn.clicked.connect(self.run_r)
        self.log_btn.clicked.connect(self.run_l)
        self.go_back.clicked.connect(self.back)

    # === Ф-ИЯ ВЫЗОВА КЛАССА ДЛЯ РЕГИСТРАЦИИ ===
    def run_r(self):
        self.reg_w = RegWindow()
        self.reg_w.setStyleSheet(stylesheet_reg)
        self.reg_w.show()
        self.close()

    # === Ф-ИЯ ВЫЗОВА КЛАССА ДЛЯ ВХОДА ===
    def run_l(self):
        self.log_w = LogWindow()
        self.log_w.setStyleSheet(stylesheet_log)
        self.log_w.show()
        self.close()

    def back(self):
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()


# === КЛАСС ОКНА РЕГИСТРАЦИИ ===
class RegWindow(QMainWindow, Ui_RegWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.reg_btn.clicked.connect(self.run)
        self.go_back.clicked.connect(self.back)
        self.psw_enter.setEchoMode(QLineEdit.EchoMode.Password)
        # Не подсматривайте пароль! Все конфедициально!

    # === Ф-ИЯ РЕГИСТРАЦИИ ===
    def run(self):
        global LOGINED, USER_ID
        name = self.username_enter.text()
        psw = self.psw_enter.text()
        try:
            # Проверяем корректность юзернейма и пароля
            check_name(name)
            check_password(psw)
        except Exception as exp:
            error(exp, self)
            return
        # Добавляем юзера в БД
        LOGINED = True
        USER_ID = append_user(name, psw)  # ф-ия также возвращает id юзера
        self.acc_w = AccWindow()
        self.acc_w.setStyleSheet(stylesheet_acc)
        self.acc_w.show()
        self.close()

    def back(self):
        self.rol_w = LogOrRegWindow()
        self.rol_w.setStyleSheet(stylesheet_rol)
        self.rol_w.show()
        self.close()


# === КЛАСС ОКНА ВХОДА В СИСТЕМУ ===
class LogWindow(QMainWindow, Ui_LogWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.log_btn.clicked.connect(self.run)
        self.go_back.clicked.connect(self.back)
        self.psw_enter.setEchoMode(QLineEdit.EchoMode.Password)
        # ----||----

    # === Ф-ИЯ ПОПЫТКИ ВХОДА ===
    def run(self):
        global LOGINED, USER_ID
        name = self.username_enter.text()
        psw = self.psw_enter.text()
        connect = sqlite3.connect('users_db.sqlite3')
        cur = connect.cursor()
        result = cur.execute("""SELECT * FROM users
                        WHERE username = ? and password = ?""", (name, psw,)).fetchall()
        connect.close()
        # Если длина не 0, то такой юзер есть, входим в систему
        if len(result):
            LOGINED = True
            USER_ID = int(result[0][0])
            self.acc_w = AccWindow()
            self.acc_w.setStyleSheet(stylesheet_acc)
            self.acc_w.show()
            self.close()
        else:
            # Иначе юзера с такими параметрами нет
            error('Неверный юзернейм или пароль!', self)

    def back(self):
        self.rol_w = LogOrRegWindow()
        self.rol_w.setStyleSheet(stylesheet_rol)
        self.rol_w.show()
        self.close()


# === КЛАСС ОКНА АККАУНТА ===
class AccWindow(QMainWindow, Ui_AccWindow):
    def __init__(self):
        global ACC_OBJ
        super().__init__()
        self.setupUi(self)
        ACC_OBJ = self
        # Копируем экземпляр класса этого окна для реализации инвентаря
        self.setFixedSize(1920, 1100)
        self.psw_btn.clicked.connect(self.show_hide)
        self.go_back.clicked.connect(self.open_choice_win)
        self.load_profile_pic.clicked.connect(self.upd_pic)
        self.log_out_btn.clicked.connect(self.log_out_func)
        self.change_name_btn.clicked.connect(self.change_username)
        self.change_psw_btn.clicked.connect(self.change_psw)
        self.del_acc_btn.clicked.connect(self.confirm_del)
        self.open_invent.clicked.connect(self.open)
        self.connect = sqlite3.connect('users_db.sqlite3')
        self.cur = self.connect.cursor()
        res = self.cur.execute("""SELECT * FROM users
                        WHERE id = ?""", (USER_ID,)).fetchall()
        # Из БД берем все данные, подставляем их в поля
        self.id_txt.setText(str(USER_ID))
        self.name_txt.setText(str(res[0][1]))
        self.psw_txt.setText(str(res[0][2]))
        self.balance_txt.setText(str(res[0][3]))
        self.psw = res[0][2]
        # Задаем настройку для пароля: Сначала он должен быть скрыт, вызываем соотв. ф-ию
        self.psw_btn.setChecked(True)
        self.show_hide()
        pic = res[0][4]
        # Если у юзера есть ава, ставим ее
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
        res = self.cur.execute(f"""SELECT id, username, balance, ans_vikt, ans_work, profile_pic,
                 filename FROM users""").fetchall()
        places = set_lists(res)[3:]
        # Из УНИВЕРСАЛЬНОГО КОРТЕЖА))) берем данные о местах в топе юзера
        self.place_txt.setText(f'Место среди балансов: #{places[0]}\nСреди решенных загадок: \
#{places[1]}\nСреди ответов на вопросы\nв викторине: #{places[2]}')

    # === Ф-ИЯ ОТКРЫТИЯ ИНВЕНТАРЯ ===
    def open(self):
        self.invent_w = InventWindow()
        self.invent_w.setStyleSheet(stylesheet_invent)
        self.invent_w.show()

    # === Ф-ИЯ ПОКАЗА/СКРЫТИЯ ПАРОЛЯ ===
    def show_hide(self):
        if self.psw_btn.isChecked():
            self.psw_txt.setText('*****')
        else:
            self.psw_txt.setText(self.psw)

    # === Ф-ИЯ ОБНОВЛЕНИЯ ФОТО ПРОФИЛЯ ===
    def upd_pic(self):
        try:
            # Открываем файлик (пытаемся открыть)
            self.filename = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
            file = open(self.filename, "rb")
            data = sqlite3.Binary(file.read())
            self.cur.execute("""UPDATE users SET profile_pic = ?, filename = ?
                                    WHERE id = ?""", (data, self.filename,
                                                      USER_ID,))
            self.connect.commit()
            self.pixmap.loadFromData(data, self.filename.split('.')[-1])
            # Если получилось, ставим аватарку
            self.image = QLabel(self)
            self.image.setPixmap(self.pixmap)
            self.image.setScaledContents(True)
            self.image.move(420, 180)
            self.image.resize(100, 100)
            self.reopen()
        except Exception as e:
            error(e, self)

    # === *Служебная* Ф-ИЯ ОБНОВЛЕНИЯ ОКНА ===
    def reopen(self):
        self.connect.close()
        self.acc_w = AccWindow()
        self.acc_w.setStyleSheet(stylesheet_acc)
        self.acc_w.show()
        self.close()

    # === Ф-ИЯ ВОЗВРАЩЕНИЯ НА СТРАНИЦУ С ИГРАМИ ===
    def open_choice_win(self):
        self.connect.close()
        self.games_w = ChoiceWindow()
        self.games_w.setStyleSheet(stylesheet_choice)
        self.games_w.show()
        self.close()

    # === Ф-ИЯ ВЫХОДА ИЗ АККАУНТА ===
    def log_out_func(self):
        global LOGINED, USER_ID
        LOGINED = False
        USER_ID = -1
        self.connect.close()
        self.ex = MainWindow()
        self.ex.setStyleSheet(stylesheet_main)
        self.ex.show()
        self.close()

    # === Ф-ИЯ СМЕНЫ ЮЗЕРНЕЙМА ===
    def change_username(self):
        new_name, ok = QInputDialog.getText(self, 'Смена юзернейма',
                                            'Введите новый юзернейм:')
        new_name = str(new_name)
        if ok:
            # Если была нажат кнопка "да", изменяем юзернейм
            tmp = self.cur.execute("""SELECT username FROM users WHERE id = ?""",
                                   (USER_ID,)).fetchall()[0][0]
            try:
                # Проверяем корректность нового юзернейма
                check_name(new_name, old=tmp)
                self.cur.execute("""UPDATE users SET username = ? WHERE id = ?""",
                                 (new_name, USER_ID,))
                self.connect.commit()
                self.reopen()
            except Exception as exp:
                error(exp, self)
                return

    # === Ф-ИЯ СМЕНЫ ПАРОЛЯ ===
    def change_psw(self):
        new_psw, ok = QInputDialog.getText(self, 'Смена пароля',
                                           'Введите новый пароль:',
                                           echo=QLineEdit.EchoMode.Password)
        new_psw = str(new_psw)
        if not ok:
            return
        # Если была нажат кнопка "да", изменяем пароль
        tmp = self.cur.execute("""SELECT password FROM users WHERE id = ?""",
                               (USER_ID,)).fetchall()[0][0]
        try:
            # Проверяем корректность нового пароля
            check_password(new_psw, old=tmp)
            self.cur.execute("""UPDATE users SET password = ? WHERE id = ?""", (new_psw, USER_ID,))
            self.connect.commit()
            self.reopen()
        except Exception as exp:
            error(exp, self)

    # === *Служебная* Ф-ИЯ ЗАПРОСА УДАЛЕНИЯ АККАУНТА ===
    def confirm_del(self):
        self.confirm = YesNoDialog()
        self.confirm.show()

    # === Ф-ИЯ УДАЛЕНИЯ АККАУНТА ===
    def del_acc(self):
        global LOGINED, USER_ID
        self.cur.execute("""DELETE from users WHERE id = ?""", (USER_ID,))
        self.connect.commit()
        self.connect.close()
        LOGINED = False
        USER_ID = -1
        # Выходим из системы
        self.ex = MainWindow()
        self.ex.setStyleSheet(stylesheet_main)
        self.ex.show()
        self.close()


# === КЛАСС ЗАПРОСА ПОДТВЕРЖДЕНИЯ УДАЛЕНИЯ АККАУНТА ===
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


# === КЛАСС ОКНА ИНВЕНТАРЯ ===
class InventWindow(QMainWindow, Ui_InventWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1920, 1100)
        self.close_window.clicked.connect(self.close)
        self.con = sqlite3.connect('users_db.sqlite3')
        self.cur = self.con.cursor()
        res = self.cur.execute(f"""SELECT inventory FROM users WHERE id = 
{USER_ID}""").fetchall()[0][0]
        if res is None:
            res = []
        else:
            res = res.split(';')
        res2 = self.cur.execute(f"""SELECT id, title FROM list""").fetchall()
        self.con.close()
        items = []
        # Из БД достаем id предметов и инвентарь юзера, делаем список (id, назв. вещи)
        for item in res2:
            items.append((str(item[0]), item[1]))
        array = []
        # Делаем список предметов юзера
        for i in items:
            if i[0] in res:
                array.append(i[1])
        self.tableInventory.setColumnCount(1)
        self.tableInventory.setRowCount(0)
        self.tableInventory.setHorizontalHeaderLabels(['Название товара'])
        # Делаем настройку таблицы
        for i, elem in enumerate(array):
            self.tableInventory.setRowCount(self.tableInventory.rowCount() + 1)
            self.tableInventory.setItem(i, 0, QTableWidgetItem(str(elem)))
        self.tableInventory.horizontalHeader().resizeSection(0, 1200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    player = QMediaPlayer()
    audio_output = QAudioOutput()
    player.setAudioOutput(audio_output)
    player.setSource(QUrl.fromLocalFile("music.mp3"))
    audio_output.setVolume(0.1)
    player.setLoops(999)
    player.play()
    sys.exit(app.exec())
