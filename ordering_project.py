
import pandas
import time
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

for key,value in menu.items():
    print(f'{key}) {value["item"]:16} | {value["price"]}$')

print('-----------------------------------------------')

class Check:
    def __init__(self,order,calculate) -> None:
        self.order=order
        self.calculate=calculate

    def calc(self):

        total=functools.reduce(lambda x,y: x+y,self.calculate )
        tax = total * 0.15    

        if len(self.order) >= 4: 
            discount_percentage= 13 / 100 * total 
            
            print('\n--------------------order summary---------------------')
            for i in self.order:
                print(f'\nitem: {i["item"]} | price: ${i["price"]}\n------------------------------------------')

            print('13% discount granted\n') 

            print(f'total: {round(discount:=total - discount_percentage,2)}$')
            
            print(f'tax: {round(tax,2)}$')

        else:
            print('\n-------------------order summary-----------------')
            for i in self.order:
                print(f'item: {i["item"]} | price: ${i["price"]}\n-------------------------------------------')

            print(f'total: {round(total,2)}$')

            print(f'tax: {round(tax,2)}$')

        when=time.localtime()
        print('----------------------------------------------------') 
        Time=time.strftime('%B %d %Y %I%p:%M:%S', when )
        print(f'date of order\n{Time}')
        print('----------------------------------------------------')

pick=None

while True: 
    pick=input('\npick the number of the item you want (click enter to checkout) ').split()

    cart=[menu[i] for i in pick]

    prices=[menu[i]['price'] for i in pick ]
    break
order=Check(cart,prices)
order.calc()
print('Enjoy your meal :)')