print('''Welcome to our toy shop "Shoppy"!
We have a few options and we hope you will find something for yourself,
to continue, please type a number of the product you want
1 - toy car, 2 - toy sword, 3 - lego, 4 - else''')
product = int(input('You option - '))
v_car=15
v_sw=12
v_lg=25

if (product > 0) and (product < 5):
    if product == 1:
        print('Good choice! Now choose how much of product you want')
        car = int(input('Number - '))
        print('In total that gonna cost ', car*v_car, '$')
        print('Now we gonna ask you for your adress to deliver products you chose')
        adress = input('Adress - ')
    elif product == 2:
        print('Good choice! Now choose how much of product you want')
        sw = int(input('Number - '))
        print('In total that gonna cost ', sw*v_sw)
        print('Now we gonna ask you for your adress to deliver products you chose')
        adress = input('Adress - ')
    elif product == 3:
        print('Good choice! Now choose how much of product you want')
        lg = int(input('Number - '))
        print('In total that gonna cost ', lg*v_lg)
        print('Now we gonna ask you for your adress to deliver products you chose')
        adress = input('Adress - ')
    elif product == 4:
        print('if you want to know more, please contact us on xxxxxxxxx number')
else:
    print('Something went wrong, please, try again')
print('-----------------------------------------------')
print('Thank you for choosing us')
print(f'Your delivery number is {product} ')