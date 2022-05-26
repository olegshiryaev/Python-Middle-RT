"""
1. Разработать класс Sphere для представления сферы в трехмерном
пространстве.
Обеспечить следующие методы класса:
■ конструктор, принимающий 4 действительных числа: радиус, и
3 координаты центра шара. Если конструктор вызывается без
аргументов, создать объект сферы с единичным радиусом и
центром в начале координат. Если конструктор вызывается с 1
аргументом, создать объект сферы с соответствующим радиусом
и центром в начале координат.
■ метод get_volume (), который возвращает действительное число
— объем шара, ограниченной текущей сферой.
■ метод get_square (), который возвращает действительное число
— площадь внешней поверхности сферы.
■ метод get_radius (), который возвращает действительное число
— радиус сферы.
■ метод get_center (), который возвращает тьюпл с 3
действительными числами — координатами центра сферы в том
же порядке, в каком они задаются в конструкторе.
■ метод set_radius (r), который принимает 1 аргумент —
действительное число, и меняет радиус текущей сферы, ничего
не возвращая.
■ метод set_center (x, y, z), который принимает 3 аргумента —
действительных числа, и меняет координаты центра сферы,
ничего не возвращая. Координаты задаются в том же порядке,
что и в конструкторе.
■ метод is_point_inside (x, y, z), который принимает 3 аргумента
— действительных числа — координаты некоторой точки в
пространстве (в том же порядке, что и в конструкторе), и
возвращает логическое значение True или False в зависимости
от того, находится эта точка внутри сферы.
"""
from math import pi


class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4 / 3 * pi * (self.radius ** 3)

    def get_square(self):
        return 4 * pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.x, self.y, self.z

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        return (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 < self.radius ** 2


s0 = Sphere(0.5)
print(s0.get_center())
print(s0.get_volume())
print(s0.is_point_inside(0, -1.5, 0))
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))
print(s0.get_radius())