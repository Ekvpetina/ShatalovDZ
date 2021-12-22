class Rectangle:
    all_rectangles = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Rectangle.all_rectangles.append(self)

    @staticmethod
    def rectangle_area(x, y):
        return x * y


    @classmethod
    def total_area(cls):
        total = 0
        for c in Rectangle.all_rectangles:
            total += c.x*c.y
        return total


class Square(Rectangle):
    def __init__(self, x, y=0):
        if y == 0:
            self.x = x
            self.y = x
        if y != 0:
            if y != x:
                raise AttributeError()
        Rectangle.all_rectangles.append(self)




Pryamougolnik = Rectangle(3, 4)
Kvadrat = Square(4)
print(Pryamougolnik.rectangle_area(3, 4))
print(Kvadrat.rectangle_area(Kvadrat.x, Kvadrat.y))
print(Pryamougolnik.total_area())
A = Square(4,6) # Проверка на правильность работы класса Square
