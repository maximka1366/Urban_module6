import  math
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = color
        self.filled = False

    def __is_valid_color(self, r, g, b):
        colors = (r, g, b)
        for i in colors:
            if  isinstance(i, int) and  0 <= i >= 255:
                return False
            else:
                return True

    def get_color(self):
        return list(self.__color)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for i in sides:
            if isinstance(i, tuple) and len(i) == self.sides_count:
                return True
            else:
                return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        if self.__sides != self.sides_count:
            return [self.__sides[0]] * self.sides_count
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, radius, *sides):
        super().__init__(color, *sides)
        self.__radius = radius

    def get_square(self):
        return math.pi * self.__radius ** 2

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = len(sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

