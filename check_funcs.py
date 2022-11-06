from exceptions import *
import sqlite3


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


def check_name(name, old=''):
    if old != '' and old == name:
        raise CurrError
    connect = sqlite3.connect('users_db.sqlite3')
    cur = connect.cursor()
    result = cur.execute("""SELECT * FROM users
                WHERE username = ?""", (name,)).fetchall()
    connect.close()
    if len(name) < 3:
        raise LenNameError
    if len(result):
        raise UsedError
