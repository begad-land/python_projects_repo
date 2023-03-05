
print('\nOFFER DAY!!\norder more than 3 items and get a 5$ discount ')

menu={
    '1':{'item':'black coffee', 'price':3.65 },
    '2':{'item': 'milk coffee' , 'price':4.25 },
    '3':{'item' :'chicken sandwich', 'price':5.35 },
    '4':{'item':'pepsi', 'price':2.99 }
    }
print('----------------MENU---------------------------\nitem               price\n')
for i in menu.values():
    print(f'{i["item"]:16} | {i["price"]}$')
print('-----------------------------------------------')

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
            print('\nfor ordering more than 3 items you get a 5$ discount\n\n-----------------order summary------------------')
            for i in self.order:
                print(f'item: {i["item"]}| price: ${i["price"]}\n------------------------------------------\n')

            print(f'your total: {total}$\nafter the discount {discount}$ ',2)
            print(f'the tax for your order is {round(tax,2)}$',2)
            print('-----------------------------------------------------')

        else:
            print('\n-------------------order summary-----------------')
            for i in self.order:
                print(f'item: {i["item"]}| price: ${i["price"]}\n-------------------------------------------\n')
            
            print(f'total: {round(total,2)}$')
            print(f'the tax for your order is {round(tax,2)}$')
            print('----------------------------------------------------')

prices=[]

cart=[]

pick=None

while True: 
    pick=input('\npick the number of the item u want (press q to end order) ').lower()
    if pick!='q':
        cart.append(menu[pick])
        prices.append(menu[pick]['price'])

    else:
        break

order=Check(cart,prices)
order.calc()