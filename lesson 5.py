'''
try:
    a = int(input('a - '))
    b = int(input('b - '))

    print('a/b >>> ', a/b)
except ZeroDivisionError:
    print('На 0 хотел поделить?😡😤')
'''
#----------------------------------------------------------------------------------------------------------------
"""
error = 'Потери⚙:'
try:
    print('Adolf Hi...; Подсчитываем результаты...')
    print(error)
    print(1999/0)
    print('Потерь. Нет.')
except NameError:
    print("Потерь нет.")
except ZeroDivisionError:
    print("КТ-ТО ПОДЕЛИЛ НА НОЛЬ😡🤬💣🔫🚀🚀")
print('------------------Джамал украл конец----------------------')
"""
#-----------------------------------------------------------------------------------------------------------------
"""
while True:
    value = input('Выбери 1 из 2-ух стулов ')
    if value == '1' or value == '2':
        break
    else:
        print('Выбери 1 из 2-ух стулов!')
print("-----------------Конец украл Джамала---------------------")
"""
#--------------------------------------------------------------------------------------------------------------
"""
def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"За базар извини, но {type (var_1)} надо переделать")
    else:
        return var_1
var1 = 10
checker(var1)
"""
#-------------------------------------------------------------------------------------------------------
"""
class BuildingError(Exception):
    def __str__(self):
        return f'Нужно много золота'\
               f'Нужно БОЛЬШЕ золота'
def check_gold(ammount_of_gold, limit_value):
    if check_gold > limit_value:
        return f'Ооооооооо... А вот так мне нравится!'
    else:
        raise BuildingError(ammount_of_gold)
gold = 999
check_gold(gold, 9999)
"""
#-------------------------------------------------------------------------------------------------------------
"""
import warnings
warnings.simplefilter("Чел в игноре", SyntaxWarning) #ignore
warnings.simplefilter("Каждое воскресенье по пятницам", ImportWarning) #always

warnings.warn("No code?🤨 No pass😤", SyntaxWarning) #no code
warnings.warn("ЧЕЛ ГДЕ ИНФА?????????", ImportWarning) #no import module
"""
#--------------------------------------------------------------------------------------------------------------
'''
str_1 = 'strings'
for i in str_1:
    print(i)
lst = [125, 'date', '456']
for i in lst:
    print(i)
tpl = ('qwerty', 125, '234')
for i in tpl:
    print(i)
set_1 ={123, 'mama', 'papa'}
for i in set_1:
    print(i)
froz = frozenset({456, 'family', '098'})
for i in froz:
    print(i)
dct = {1,2,'papa'}
for i in dct:
    print(i)

str1 = "mother"
print(set(str1))
print(list(str1))

lst_2 = [123, [178, 'str', 987], 'itstep']
iterator = iter(lst_2)
print(next(iterator))
print(next(iterator))
print(next(iterator))

for elem in iterator:
    print(elem)
class Counter:
    def __init__(self, max_number):
        self.i=0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
count=Counter(5)
for elem in count:
    print (elem)
print(count.__next__())
print(count.__iter__())
print(next(count))
print(next(count))
print(next(count))
'''
#------------------------------------------------------------------------------------------------------------------
'''
def raise_to_the_degrees(number, max_degree):
    i=0
    for _ in range(max_degree):
        yield number ** i
        i += 1
res = raise_to_the_degrees(122345, 10)
print(res)
for _ in res:
    print(_)
print('-----------------------------------------------------------------------------------------')
for _ in res:
    print(_)
def raise_ro_the_degrees2(number):
    i=0
    while True:
        #yield number ** 1
        #i+=1
        result = number ** i
        yield result
        if result > 100 ** 20:
            return
        i += 1
res = raise_ro_the_degrees2(134)
print(res)
for _ in res:
    print(_)
'''
#---------------------------------------------------------------------------------------------------------
class Helper:
    def __init__(self,work):
        self.work = work
    def __call__(self, work):
        return f'Помогу за 50 гривен с твоей {self.work}'\
               f'Либо иди на {work} выбор за тобой'
helper = Helper('no job?😰')
print(helper('Убирать помои🤯🙄'))
def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'Потерь нет{exc}')
        else:
            print(f'Потерь нет. Потери:{result}')
    return checker
def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
calculate('2+2')