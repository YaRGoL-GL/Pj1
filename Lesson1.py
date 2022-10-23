'''
    def summary():
        x = int(input('x= '))
        y = int(input('y= '))

        return print(f'Добуток x**y = {x ** y}')

    summary()
'''


class Bobloc():
    print('New bobloc update😳')
    amount_of_bobuc = 0
    def __init__(self, height = -999999 ):
        self.height = height
        Bobloc.amount_of_bobuc +=1
        print('No bobuc??🤨😎')
first_bobuc = Bobloc()
second_bobuc = Bobloc()
tenth_bobuc = Bobloc(height = -444432345)
#Bobloc.__init__(self=first_bobuc)
print('Ur first bobuc is🥶😳 =', first_bobuc.height)
print('Ur second bobuc is🥶😳 =', second_bobuc.height)
print('Ur tenth bobuc is🥶😳 =', tenth_bobuc.height)
print('Ur first bobuc income🤑 =', first_bobuc.amount_of_bobuc)
print('Ur second bobuc income🤑 =', second_bobuc.amount_of_bobuc)
print('Ur tenth bobuc income🤑 =', tenth_bobuc.amount_of_bobuc)