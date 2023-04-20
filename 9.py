# 1) реализовать дескрипторы для любых двух классов
# 1
class Checkmi:

    def __set__(self, instance, value):
        if type(value) is str:
            raise ValueError("Данная программа принимает только числа для вычисления")
        instance.__dict__[self.my_vari] = value

    def __set_name__(self, owner, my_vari):
        self.my_vari = my_vari


class Road:
    _length = Checkmi()
    _width = Checkmi()
    mass = Checkmi()
    tol = Checkmi()

    def __init__(self, _length, _width, mass, tol):
        self._length = _length
        self._width = _width
        self.mass = mass
        self.tol = tol

    def asf(self):
        res = (float(self._length) * float(self._width) * float(self.mass)) * float(self.tol)
        return res


a = Road(20, 5000, 25, 0.05)
b = a.asf()
print(int(b // 1000), "т")

# 2


class Checkmi:

    def __set__(self, instance, value):
        if type(value) is not str:
            raise ValueError("Имя, Фамилия или Должность не могут быть числом")
        instance.__dict__[self.my_vari] = value

    def __set_name__(self, owner, my_vari):
        self.my_vari = my_vari


class Worker:
    name = Checkmi()
    surname = Checkmi()
    position = Checkmi()

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Имя: {self.name}, Фамилия: {self.surname}")

    def get_total_income(self):
        print(f"Общий доход равен: {sum(self._income.values())}")


a = Position("Джонотан", "Джостар", "Президент компании", 300000, 100000)
a.get_full_name()
print(f"Должность: {a.position}")
a.get_total_income()


# 2) реализовать метакласс. позволяющий создавать всегда один и тот же объект класса (см. урок)
class TestMeta(type):
    exaple = None

    def __call__(self):
        if self.exaple == None:
            self.exaple = super().__call__()
        return self.exaple


class MyClass(metaclass=TestMeta):
    pass


fir = MyClass()
seс = MyClass()

print(fir is seс)
