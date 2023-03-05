
print('OFFER DAY!!\norder more than 3 items and get a 5$ discount ')

print()
print('__________Menu_____________')
print('   items        price')
menu={
    '1':{'item':'black coffee', 'price':3 },
    '2':{'item': 'milk coffee' , 'price':4 },
    '3':{'item' :'chicken sandwich', 'price':5 },
    '4':{'item':'pepsi', 'price':2 }
    }

for i,y in menu.items():
    print(f'{i}.{y["item"]} | {y["price"]}$')

class Check:
    def __init__(self,order,calculate) -> None:
        self.order=order
        self.calculate=calculate

    def calc(self):

    
        total=0
        for i in self.calculate :
            total+=i
        tax = total * 0.12

        if len(self.order) > 3: 
            discount=total - 5
            print('for ordering more than 3 items you get a 5$ discount\n---------------order summary---------------')
            for i in self.order:
                print(f'your order: {i["item"]}| price: {i["price"]}$', end='   ' )
            print()
            print(f'your total: {total}$\nafter the discount {discount}$ ')
            print(f'the tax for your order is {round(tax,2)}$')
            print('-----------------------------------------------------')

        else:
            print('--------------------order summary------------------')
            for i in self.order:
                print(f'your order: {i["item"]}| price: {i["price"]}$', end='   ' )
            print()    
            print(f'total: {total}$')
            print(f'the tax for your order is {round(tax,2)}$')
            print('----------------------------------------------------')

prices=[]

cart=[]

pick=None

while True: 
    pick=input('pick the number of the item u want (press q to end order) ').lower()
    if pick!='q':
        cart.append(menu[pick])
        prices.append(menu[pick]['price'])
        
    else:
        break

order=Check(cart,prices)
order.calc()