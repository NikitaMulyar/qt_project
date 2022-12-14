from data.exceptions import *
import sqlite3


dict_words = set()
some_words = set()
f_o = open("data/top 10000 passwd.txt", encoding="utf-8", mode="r")
f_o2 = open("data/top-9999-words.txt", encoding="utf-8", mode="r")
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


# === Ф-ИЯ ПРОВЕРКИ ПАРОЛЯ ===
def check_password(psw, old=''):
    if old != '' and psw == old:
        raise CurrPswError
    if len(psw) < 8:
        raise LengthError
    if psw.lower() == psw or psw.upper() == psw:
        raise LetterError
    for i in psw:
        if i.isdigit():
            break
    else:
        raise DigitError
    # Проверим пароль на подряд идущие символы
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


# === Ф-ИЯ ПРОВЕРКИ ЮЗЕРНЕЙМА ===
def check_name(name, old=''):
    if old != '' and old == name:
        raise CurrError
    connect = sqlite3.connect('data/users_db.sqlite3')
    cur = connect.cursor()
    result = cur.execute("""SELECT * FROM users
                WHERE username = ?""", (name,)).fetchall()
    connect.close()
    if len(name) < 3:
        raise LenNameError
    if len(result):
        raise UsedError


# === Ф-ИЯ ПРОВЕРКИ БАЛАНСА ===
def check_balance(stavka, id):
    connect = sqlite3.connect('data/users_db.sqlite3')
    cur = connect.cursor()
    result = cur.execute(f"""SELECT balance FROM users WHERE id = {id}""").fetchall()[0][0]
    connect.close()
    return result >= stavka


# === Ф-ИЯ ПРОВЕРКИ СТАВКИ ===
def check_stavka(stavka, id):
    if '-' not in stavka and not stavka.isdigit() or \
            '-' in stavka and stavka[1:].isdigit():
        raise NotNumberError
    summ = int(stavka)
    if summ < 100 or summ > 100000:
        raise NotPositiveNumberError
    if not check_balance(summ, id):
        raise BigSummError


# === Ф-ИЯ ПРОВЕРКИ НАЛИЧИЯ ПРЕМИУМА ===
def check_premium(invent):
    if invent is None:
        return 1
    else:
        invent1 = invent.split(';')
        if isinstance(invent1, list):
            if '1' in invent1:
                return 1.5
        elif isinstance(invent1, str):
            if invent1 == '1':
                return 1.5
