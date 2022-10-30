'''
class Student():
    amount_of_students = 0
    height = 160
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students += 1
    def grow(self,height=1):
        self.height += height

Maxim = Student()
Maxim.grow(height=17)
Jamal = Student(height =160)
Jamal.grow(height=10)
print('Maxim = ', Maxim.height )
print('Jamal🧑🏿 = ', Jamal.height )

-----------------------------------------------

class Student():
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return f'Your name is {self.name}'
    def __del__(self):
        print(f'Training is over. {self.name} is pro now😎')
Jamal = Student(name='Jamal🧑🏿')
Maxim = Student(name='Maxim👨🏿')
print(Jamal)
print(Maxim)

---------------------------------------

class Student:
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height
    def __bool__(self):
        return self.name !=None
    def __len__(self):
        return self.height
Artem=Student(name='Artem🥶', height=175)
Nazarspeed=Student(name='Nazarspeed1😨🤯', height=95)
print(Artem.name)
print(bool(Artem))
print(Artem.__bool__())
print(len(Artem))
print(Artem.__len__())
print(Nazarspeed.name)
print(bool(Nazarspeed))
print(Nazarspeed.__bool__())
print(len(Nazarspeed))
print(Nazarspeed.__len__())
'''
class Avto:
    def __init__(self, model, speed, color):
        self.model = model
        self.speed = speed
        self.color = color
Lada=Avto(color='red', speed='999km/h😎', model='x243')
print(f'Цвет Лады - {Lada.color}')
print(f'Скорость Лады - {Lada.speed}')
print(f'Модель Лады - {Lada.model}')
