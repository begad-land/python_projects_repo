
print('\nOFFER DAY!!\norder more than 3 items and get a 5$ discount ')

menu={
    '1':{'item':'black coffee', 'price':3.65 },
    '2':{'item': 'milk coffee' , 'price':4.25 },
    '3':{'item' :'chicken sandwich', 'price':5.35 },
    '4':{'item':'pepsi', 'price':1.99 },
    '5':{'item':'Hotdog', 'price':2.45}
    }
print('----------------MENU---------------------------\nitem                  price\n')
counter=1
for i in menu.values():
    print(f'{counter}) {i["item"]:16} | {i["price"]}$')
    counter+=1
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
            print('\n--------------------order summary---------------------')
            for i in self.order:
                print(f'\nitem: {i["item"]}| price: ${i["price"]}\n------------------------------------------')

            print('\nfor ordering more than 3 items you get a 5$ discount\n')

            print(f'total: {round(total,2)}$\npost discount: {round(discount,2)}$ ')

            print(f'order tax: {round(tax,2)}$')
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
    pick=input('\npick the number of the item u want (enter q to end order) ').lower()
    if pick!='q':
        cart.append(menu[pick])
        prices.append(menu[pick]['price'])

    else:
        break

order=Check(cart,prices)
order.calc()