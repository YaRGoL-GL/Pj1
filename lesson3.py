'''
class Human:
    def __init__(self, name='Human'):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passangers = []
    def add_passangers(self, human):
        self.passangers.append(human)
    def print_passangers_names(self):
        if self.passangers != []:
            print(f'Names of {self.brand} passangers:')
            for passangers in self.passangers:
                print(passangers.name)
        else:
            print(f"There are no passangers in {self.brand}")
nick = Human('Nick')
john = Human('John')
car = Auto('BMW')
carW = Auto('Hyindai')

car.add_passangers(john)
carW.add_passangers(nick)
car.print_passangers_names()
carW.print_passangers_names()
'''

data = 30
day = 'Sonntag'
month = "Oktober"
print('Heute ist',data, month,'-', day,'.')
# f-Lines
print(f'Heute ist {data} {month} {day}.')
print(f'Heute ist {data:_^10} {month:$>15} {day:#<15}.') # > < ^ Расстояние и направления символов
# format
print('Heute ist {} {} {}.'.format(data,month,day))
print('Heute ist {:@^9} {:%^24} {:*<11}.'.format(data,month,day)) # > < ^ Расстояние и направления символов
print('Heute ist {data} {month} {day}.'.format(data=31,month="Oktober",day='Monday'))

a = 10
b = 7
print(f'Die Summe {a} und {b} is gleich {a + b}')
print(f'Die Multiplikation {a} und {b} is gleich {a * b}')
