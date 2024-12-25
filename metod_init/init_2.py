class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}:{x.price}' for x in self.goods]


class Base:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Base):
    pass


class TV(Base):
    pass


class Notebook(Base):
    pass


class Cup(Base):
    pass


cart = Cart()
cart.add(TV('Samsung', 20000))
cart.add(TV('LG', 30000))
cart.add(Table('круглый', 5000))
cart.add(Notebook('HP', 50000))
cart.add(Notebook('acer', 30000))
cart.add(Cup('пивная', 200))


print(cart.get_list())
