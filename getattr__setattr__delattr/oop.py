class Graph:
    LIMIT_Y = [0, 10]
    
    def set_data(self, data):
        self.data = data
        
    def draw(self):
        print(*[x for x in self.data if (Graph.LIMIT_Y[0] <= x <= Graph.LIMIT_Y[1])])
        
graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])

graph_1.draw() 




class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
setattr(fig1, 'start_pt', (10, 5))
setattr(fig1, 'end_pt', (100, 20))
setattr(fig1, 'color', 'blue')
delattr(fig1, 'color')

print(*fig1.__dict__, end='')


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
if 'job' in p1.__dict__:
    result = True
else:
    result = False

print(result)



class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]

tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")

print(*tr.translate("go"))