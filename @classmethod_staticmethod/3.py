from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    set_chars = set(CHARS_FOR_NAME)

    @classmethod
    def check_card_number(cls, number) -> bool:
        """проверяет строку с номером карты и возвращает булево значение True,
        если номер в верном формате и False - в противном случае. Формат номера следующий:
        XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)."""
        if type(number) != str:
            return False
        s = number.split('-')
        if len(s) != 4:
            return False
        if not all(map(lambda x: len(x) == 4, s)):
            return False

        return all(map(lambda x: x.isdigit(), s))

    @classmethod
    def check_name(cls, name) -> bool:
        """проверяет строку name с именем пользователя карты.
        Возвращает булево значение True, если имя записано верно и False"""
        if type(name) != str:
            return False
        s = name.split()
        if len(s) != 2:
            return False

        return all(map(lambda x: set(x) < cls.set_chars, s))


                                # через регулярки
class CardCheck:
    CARD_NUMBER_REGEX = re.compile(r"[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}")
    NAME_REGEX = re.compile(r"^[A-Z0-9]{0,}\s[A-Z0-9]{1,}$")

    @classmethod
    def check_card_number(cls, number):
        if cls.CARD_NUMBER_REGEX.fullmatch(number):
            return True
        return False

    @classmethod
    def check_name(cls, name):
        if cls.NAME_REGEX.fullmatch(name):
            return True
        return False
