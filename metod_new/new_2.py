TYPE_OS = 2 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"



class Dialog:
    """Класс Dialog должен создает объекты класса DialogWindows, если переменная TYPE_OS = 1"""

    def __new__(cls, *args, **kwargs):
        obj = None
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)

        else:
            obj = super().__new__(DialogLinux)

        obj.name = args[0]

        return obj


dlg = Dialog('Name')

print(dlg)
