'''
class Human:
    height = 170
    Jheight = 9
    society = 50
class Student(Human):
    society = 0
class Worker(Human):
    society =  100
nick = Student()
jamal = Worker()

print ('Nick height - ',nick.height)
print ('Jamal height - ',jamal.Jheight)
print ('Nick society - ',nick.society)
print ('Jamal society - ',jamal.society)
------------------------------------------------------------
class Grandparent():
    height = 160
    society = 60
    age = 65
    def __init__(self):
        print('Grandparent height - ', self.height)
        print('Grandparent society - ', self.society)
        print('Grandparent age - ', self.age)
class Parent(Grandparent):
    age = 30
    def __init__(self):
        print('Parent height - ', self.height)
        print('Parent society - ', self.society)
        print('Parent age - ', self.age)
class Child(Parent):
    height = 95
    def __init__(self):
        print('Child height - ', self.height)
        print('Child society - ', self.society)
        print('Child age - ', self.age)
Jamal = Grandparent()
-------------------------------------------------------
class Exprescion:
    def __exprecsion(self):
        print("Incredible!")
    def _hello(self):
        print("Hello!")
obj_some = Exprescion()
obj_some._hello()
obj_some._Exprescion__exprecsion()
-------------------------------------------------------
class Hello_world:
    hello="Hello"
    _hello="Hi"
    __hello="STOP HELLO'ING ON ME"
    def __init__(self):
        self.world = 'World!'
        self._world = 'Universe'
        self.__world = 'YOU DAM PIECE OF...'
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
class Hi(Hello_world):
    def hi_printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
hello = Hello_world()
hello.printer()
print("****************************")
hi = Hi()
hi.hi_printer()
------------------------------------------------------
'''
class Hello:
    def __init__(self):
        print('hello')
class Hello_world(Hello):
    def __init__(self):
        super().__init__()
        print('World')
hello_world = Hello_world()

