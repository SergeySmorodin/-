# Объявите три класса геометрических фигур: Line, Rect, Ellipse. 
# Должна быть возможность создавать объекты каждого класса следующими командами:

# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего 
# правого и нижнего левого углов (произвольные числа). В каждом объекте 
# координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и 
# ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.

# Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается 
# случайно (или Line, или Rect, или Ellipse). Координаты также генерируются 
# случайным образом (числовые значения). Все объекты сохраните в списке elements.

# В списке elements обнулите координаты объектов только для класса Line.

# P.S. На экран в программе ничего выводить не нужно.
# from random import randint

# class Line:

#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)


# class Rect:
               
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)

# class Ellipse:

#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)


# elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4) for n in range(217)]
# for obj in elements:
#     if isinstance(obj, Line):
#         obj.sp = obj.ep = 0, 0




# a = int(input())

# gen = (abs(x) for x in range(-a, a+1))
# gen2 = (x**3 for x in gen)

# for i in range(4):
#     print(next(gen2), end=' ')



# string = 'abcdefghijklmnopqrstuvwxyz'

# gen = (f"{string[x]}{string[i]}" for x in range(len(string)) for i in range(len(string)))

# print(*list(gen)[:50])


cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]


gen = (cities[i % len(cities)] for i in range(1000000))
 
# print(*(next(gen) for i in range(20)))

# for i in range(20):
#     index = i % len(cities)
#     print(cities[index])



# Тут требуется 20 раз подсчитать значение вот этого  0.5 * pow(x, 2) - 2.0 в диапазоне от a до b включительно с шагом 0.01. 
# Если как в примере диапазон от 0 до 10 то первое значение подставляем 0, и считаем что получается, далее подставляем 0.01 и считаем, 
# затем 0.02 и т.д. пока не дойдем до b которое тут в примере 10. Попутно не забывая округлять все до сотых.
# Ну а потом первые 20 значений выводим на экран. 
a, b = 0, 10


def calculate_values(a, b, step=0.01):
    results = []
    x = a
    
    while x <= b:
        value = 0.5 * pow(x, 2) - 2.0
        results.append(round(value, 2))
        x += step
        
        # if len(results) >= 20:
        #     break
    
    return results


values = calculate_values(a, b)

# # Выводим первые 20 значений
# for i, value in enumerate(values):
#     print(f"Значение {i + 1}: {value}")

print(*values[:20])