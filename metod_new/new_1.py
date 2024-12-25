class SingletonFive:
    __instance = None
    __count = 0


    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count += 1

        return cls.__instance


    def __init__(self, name):
        self.name = name



objs = [SingletonFive(str(n)) for n in range(10)]

print(objs)

# a = SingletonFive('Первый')
# print(a.__dict__, id(a))
# b = SingletonFive('Второй')
# print(b.__dict__, id(b))
# c = SingletonFive('Третий')
# print(c.__dict__, id(c))
# d = SingletonFive('Четвертый')
# print(d.__dict__, id(d))
# e = SingletonFive('Пятый')
# print(e.__dict__, id(e))
# f = SingletonFive('шестой')
# print(f.__dict__, id(f))
# z = SingletonFive('седьмой')
# print(z.__dict__, id(z))