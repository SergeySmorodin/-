from random import randint


class Cell:
    """для представления клетки игрового поля"""

    def __init__(self, around_mines=0, mine=False):
        """around_mines - число мин вокруг данной клетки поля;
        mine - наличие/отсутствие мины в текущей клетке (True/False)
        fl_open - открыта/закрыта клетка - булево значение"""
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    """для управления игровым полем, размером N x N клеток."""
    def __init__(self, N, M):
        """N - размер поля; M - общее число мин на поле"""
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        self.init()


    def init(self):
        """инициализация поля с новой расстановкой M мин"""
        m = 0
        while m < self._m:
            i = randint(0, self._n-1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self._n and 0 <= y+j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        """отображение поля в консоли в виде таблицы чисел открытых клеток"""
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))

pole_game = GamePole(10, 12)
pole_game.show()
