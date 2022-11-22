class PasswordError(Exception):
    pass


class UsernameError(Exception):
    pass


class SummError(Exception):
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


class CurrPswError(PasswordError):
    def __str__(self):
        return 'Нельзя указывать текущий пароль!'


class UsedError(UsernameError):
    def __str__(self):
        return 'Такой юзернейм уже занят!'


class CurrError(UsernameError):
    def __str__(self):
        return 'Нельзя указывать текущий юзернейм!'


class LenNameError(UsernameError):
    def __str__(self):
        return 'Длина юзернейма должна быть больше либо равна 3!'


class NotPositiveNumberError(SummError):
    def __str__(self):
        return 'Сумма ставки должна быть от 100 до 10000!'


class NotNumberError(SummError):
    def __str__(self):
        return 'Ставка должна быть числом!'


class BigSummError(SummError):
    def __str__(self):
        return 'Сумма ставки должна быть меньше либо равна сумме баланса!'
