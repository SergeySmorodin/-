from string import ascii_lowercase, digits
import re


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        res = f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

        return res

    @classmethod
    def check_name(cls, name):
        """Проверяет корректность имени:
        - длина имени не менее 3 символов и не более 50;
        - в именах могут использоваться только символы русского,
            английского алфавитов, цифры и пробелы"""
        if len(name) < 3 or len(name) > 50:
            raise ValueError("длина имени должна быть от 3 до 50 символов")

        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("имя может содержать только буквы, цифры и пробелы")

        # через цикл
        # for i in name:
        #     if i not in CHARS_CORRECT:
        #         raise ValueError("имя может содержать только буквы, цифры и пробелы")

        # Используем регулярное выражение для проверки разрешенных символов
        # pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9\s]+$'
        # if not re.match(pattern, name):
        #     raise ValueError("имя может содержать только буквы, цифры и пробелы")


class PasswordInput(TextInput):

    def get_html(self):
        res = f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

        return res


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
