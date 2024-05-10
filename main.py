# Задание 1.
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=, >=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __add__(self, change):
        self.radius += change
        return self

    def __sub__(self, change):
        self.radius -= change
        return self

    def __iadd__(self, change):
        self.radius += change
        return self

    def __isub__(self, change):
        self.radius -= change
        return self


c1 = Circle(5)
c2 = Circle(6)
print(c1 == c2)
print(c1 > c2)
print(c1 < c2)
print(c1 >= c2)
print(c1 <= c2)
c1 + 2
print(c1.radius)
c2 - 2
print(c2.radius)
c1 -= 2
print(c1.radius)
c2 += 2
print(c2.radius, '\n')


# Задание 2.
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b >= 0:
            return f'{self.a} + {self.b}i'
        else:
            return f'{self.a} - {abs(self.b)}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)

    def __truediv__(self, other):
        new_a = self.a * other.a + self.b * other.b
        new_b = self.b * other.a - self.a * other.b
        denominator = other.a ** 2 + other.b ** 2
        return Complex(new_a/denominator, new_b/denominator)


com1 = Complex(2, 5)
com2 = Complex(3, 4)
print(com1 + com2)
print(com1 - com2)
print(com1 * com2)
print(com1 / com2, '\n')


# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# ■ Проверка на равенство типов самолетов (операция
# = =);
# ■ Увеличение и уменьшение пассажиров в салоне
# самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному
# количеству пассажиров на борту (операции >
# < <= >=).

class Airplane:
    def __init__(self, type_of_airplane, number_of_seats, max_number_of_seats):
        self.type_of_airplane = type_of_airplane
        self.number_of_seats = number_of_seats
        self.max_number_of_seats = max_number_of_seats

    def __eq__(self, other):
        return self.type_of_airplane == other.type_of_airplane

    def __add__(self, change):
        self.number_of_seats += change
        return self

    def __sub__(self, change):
        self.number_of_seats -= change
        return self

    def __iadd__(self, change):
        self.number_of_seats += change
        return self

    def __isub__(self, change):
        self.number_of_seats -= change
        return self

    def __gt__(self, other):
        return self.max_number_of_seats > other.max_number_of_seats

    def __lt__(self, other):
        return self.max_number_of_seats < other.max_number_of_seats

    def __ge__(self, other):
        return self.max_number_of_seats >= other.max_number_of_seats

    def __le__(self, other):
        return self.max_number_of_seats <= other.max_number_of_seats


a1 = Airplane('passenger plane', 45, 70)
a2 = Airplane('passenger plane', 35, 80)
print(a1 == a2)
a1 + 2
print(a1.number_of_seats)
a2 - 5
print(a2.number_of_seats)
print(a1 > a2, '\n')


# Задание 4.
# Создать класс Flat (квартира). Реализовать перегруженные
# операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, square, price):
        self.square = square
        self.price = price

    def __eq__(self, other):
        return self.square == other.square

    def __ne__(self, other):
        return self.square != other.square

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


f1 = Flat(50, 2000000)
f2 = Flat(75, 3000000)

print(f1 == f2)
print(f1 != f2)
print(f1 > f2)
print(f1 < f2)
print(f1 >= f2)
print(f1 <= f2)
