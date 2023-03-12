import functools
print('\nOFFER DAY!!\norder four or more items for a 13% discount ')

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
        tax = total * 0.15    

        if len(self.order) >= 4: 
            discount_percentage= 13 /100 * total 
            
            print('\n--------------------order summary---------------------')
            for i in self.order:
                print(f'\nitem: {i["item"]} | price: ${i["price"]}\n------------------------------------------')

            print('13% discount granted \n')

            print(f'\ntax: {round(tax,2)}$')

            print(f'total: {round(discount:=total - discount_percentage,2)}$')
            print('-----------------------------------------------------')

        else:
            print('\n-------------------order summary-----------------')
            for i in self.order:
                print(f'item: {i["item"]}| price: ${i["price"]}\n-------------------------------------------\n')

            print(f'tax: {round(tax,2)}$')

            print(f'total: {round(total,2)}$')
            print('----------------------------------------------------')

prices=[]

cart=[]

pick=None

while True: 
    pick=input('\npick the number of the item you want (click enter to checkout) ').split()
    
    for i in pick:
        cart.append(menu[i])
        prices.append(menu[i]['price'])
    break

order=Check(cart,prices)
order.calc()
print('Enjoy your meal :)')